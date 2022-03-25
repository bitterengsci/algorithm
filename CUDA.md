<!-- TOC -->

- [1. CUDA](#1-cuda)
  - [1.1. Grid, Block, Thread](#11-grid-block-thread)
  - [1.2. Memory Transfer](#12-memory-transfer)
  - [1.3. Error Handling](#13-error-handling)
  - [1.4. Device Properties](#14-device-properties)
- [2. CUDA Execution Model](#2-cuda-execution-model)
- [3. CUDA Memory Model](#3-cuda-memory-model)
- [4. CUDA Streams & Events](#4-cuda-streams--events)
  - [4.1. __restrict__](#41-restrict)
- [5. Memory Hierarchy/Type](#5-memory-hierarchytype)
- [6. Pytorch](#6-pytorch)
- [7. TensorRT](#7-tensorrt)
- [8. Examples](#8-examples)

<!-- /TOC -->


char 1 byte = 8 bits
int 4 bytes
float 4 bytes


# 1. CUDA
CPU:
- latency device with high lock speed
- small number of cores
- have optimization hardware like branch predictors
- context switching by software

GPU:
- throughput device with low lock speed
- thousands of cores
- context switching by hardware
- can switch between thread if one thread stalls
- thread schedulers and dispatch units are implemented in hardware

Heterogeneous Computing: systems use more than one kind of processors or cores.

Basic steps of a CUDA Program:
1. data initialization from CPU
2. transfer data from CPU context to GPU context
3. kernel launch with grid/block size
4. transfer results back to CPU context

Host Code (main function and run in CPU) <--> Device Code (run in GPU)

```cpp
dim3 var(X, Y, Z);   // var.x, var.y, var.z
kernel <<< NumBlocks, ThreadPerBlock >>> (arguments); 
cudaDeviceSynchronize();
cudaDeviceReset();

// limitation for block size x <= 1024, y <= 1024, z <= 64 and x * y * z <= 1024
// limitation for number of thread block in each dimension:
// x: 2**32 - 1, y: 65536, z: 65536     why?????????
```


## 1.1. Grid, Block, Thread
Grid: a collection of all the threads launch for a kernel
Block: threads in a grid are organized as group (i.e., block)
Thread: 

CUDA runtime uniquely initializes threadIdx (dim3 type) for each thread, depending on where that particular thread is located in the thread block. 

```cpp
// global (unique) index with multi-dimensional grids of multi-dimensional blocks of threads
// Use threadIdx, blockIdx, blockDim, gridDim (all in dim3) to calculate array indices (blockId/threadId in a linear way...)

// 1D grid of 1D blocks
__device__ int getGlobalIdx_1D_1D() {
    return blockIdx.x * blockDim.x + threadIdx.x; 
}
// 1D grid of 2D blocks
__device__ int getGlobalIdx_1D_2D() {
    return blockIdx.x * blockDim.x * blockDim.y
            + threadIdx.y * blockDim.x + threadIdx.x;
}
// 1D grid of 3D blocks
__device__ int getGlobalIdx_1D_3D(){
    return blockIdx.x * blockDim.x * blockDim.y * blockDim.z
            + threadIdx.z * blockDim.y * blockDim.x
            + threadIdx.y * blockDim.x + threadIdx.x;
}
// 2D grid of 1D blocks
__device__ int getGlobalIdx_2D_1D(){
    int blockId = blockIdx.y * gridDim.x + blockIdx.x;
    int threadId = blockId * blockDim.x + threadIdx.x;  
    return threadId;
}
// 2D grid of 2D blocks
__device__ int getGlobalIdx_2D_2D(){
    int blockId = blockIdx.x + blockIdx.y * gridDim.x; 
    int threadId = blockId * (blockDim.x * blockDim.y)
                    + threadIdx.y * blockDim.x + threadIdx.x; 
    return threadId;
}
// 2D grid of 3D blocks
__device__ int getGlobalIdx_2D_3D(){
    int blockId = blockIdx.x + blockIdx.y * gridDim.x;
    int threadId = blockId * (blockDim.x * blockDim.y * blockDim.z)
                    + threadIdx.z * (blockDim.x * blockDim.y)
                    + threadIdx.y * blockDim.x + threadIdx.x; 
    return threadId;
}
// 3D grid of 1D blocks
__device__ int getGlobalIdx_3D_1D(){
    int blockId = blockIdx.x + blockIdx.y * gridDim.x + blockIdx.z * gridDim.x * gridDim.y;
    int threadId = blockId * blockDim.x + threadIdx.x; 
    return threadId;
}
// 3D grid of 2D blocks
__device__ int getGlobalIdx_3D_2D(){
    int blockId = blockIdx.x + blockIdx.y * gridDim.x + blockIdx.z * gridDim.x * gridDim.y;
    int threadId = blockId * (blockDim.x * blockDim.y)
                + threadIdx.y * blockDim.x + threadIdx.x;
    return threadId;
}
// 3D grid of 3D blocks
__device__ int getGlobalIdx_3D_3D(){
    int blockId = blockIdx.x + blockIdx.y * gridDim.x + blockIdx.z * gridDim.x * gridDim.y;
    int threadId = blockId * (blockDim.x * blockDim.y * blockDim.z)
                    + threadIdx.z * blockDim.x * blockDim.y
                    + threadIdx.y * blockDim.x + threadIdx.x;
    return threadId;
}
```

## 1.2. Memory Transfer
```cpp
int *h_A;
h_A = (int*)malloc(sizeof(int) * N);

int *d_A;
// cudaMalloc ( void** devPtr, size_t size );
cudaMalloc((void**) &d_A, sizeof(int) * N);
// cudaMemcpy ( void* dst, const void* src, size_t count, cudaMemcpyKind kind/direction );
cudaMemCpy(d_A, d_h, size, cudaMemcpyHostToDevice);  

// Initializes or sets device memory to a value
// cudaMemset ( void* devPtr, int value, size_t count );
// cudaFree ( void* devPtr );
```

## 1.3. Error Handling
- compile time errors
- run time errors
```cpp
dim3 block(block_size);
dim3 grid( size / block.x + 1);

kernel <<< grid, block >>> (args);
cudaDeviceSynchronize();

cudaError error;
error = cuda_func(...);   // e.g., error = cudaMalloc()
if (error != cudaSuccess)  
    fprintf(stderr, "Error: %s \n", cudaGetErrorString(error));
```
[Topic]: Timing
```cpp
#include <time.h>

clock_t start, end;  // start = clock();
printf("time %4.6f", (double)((double)(end - start) / CLOCKS_PER_SEC));
```

## 1.4. Device Properties
- name: ASCII string identifying the device
- major/minor: major and minor revision numbers defining the device's compute capability
- totalGlobalMem: total amount of global memory available on the device in bytes
- maxThreadsPerBlock: max number of threads/registers per block
- maxThreadsDim[3]: max size of each dimension of a block
- maxGridSize[3]: max size of each dimension of a grid
- clockRate: clock frequency in kilohertz
- sharedMemPerBlock: max amount of shared memory available to a thread block in bytes
- warp size

```cpp
int deviceCount = 0;
cudaGetDeviceCount(&deviceCount);

int deviceNum = 0;
cudaDeviceProp iProp;
cudaGetDeviceProperties(&iProp, deviceNum);
// iProp.name iProp.multiProcessorCount iProp.clockRate
```

# 2. CUDA Execution Model
Computer Architectures:
- SISD: single instruction single data
- SIMD: single instruction multiple data
- MISD: multiple instruction single data
- MIMD: multiple instruction multiple data

SIMT: single instruction multiple threads --> CUDA

Thread blocks is going to execute in single SM. Multiple thread block can be execute simultaneously on same SM depending on resource limitation on SM.

But one thread block cannot be executing in multiple SM. If device cannot run single block in one SM, then error will return for that kernel launch.

warps: 32 consecutive threads (basic unit of execution in a SM)

Once a thread block is scheduled to an SM, threads in the block are further partitioned into warps. All threads in a warp are executed in SIMT fasion.

Warp size is 32. Even run thread block with single thread, CUDA runtime will assign single warp (32 threads). Only 1 thread will be active and the rest 31 threads will be in inactive state. (waste of resource in SM)

Warp Divergence: threads in the same warp execute different instructions
    control flow statements (if-else, switch) gives a hint of divergent code
```cpp
if (tid % 2 == 0) { } else { }  // warp divergence
if (tid / 32 < 1) { } else { }  // no warp divergence
// condition checks may not generate divergence under some circumstances.
```

Branch Efficiency = (#branches - #divergent branches) / #branches

branch is a path of execution for the threads in a warp

warp
- selected warp: active warp
- stalled warp:
- eligible warp: 
  - 32 CUDA cores should free for execution + all arguments to the current instruction for that warp ready

Latency: number of clock cycles between instruction being issued and being completed.
- arthimetic instruction latency
- memory operation latency

Occupancy = active warps / maximum warps per SM

If a kernel is not bandwidth-bound or computation-bound, then increasing occupancy will not necessarily increase performance. Increasing occupancy can have effects, such as additional instructions, more register spills to local memory which is an off-chip memory, more divergent branches.

nvprof Profile modes: summary mode; GPU and API trace mode; event metrics summary mode; event metrics trace mode

```cpp
// reduce
// neighbored pairs approach
for(int offset=1; offset < blockdim.x; offset *= 2){
    if( tid % (2 * offset) == 0) {
        input[tid] += input[tid + offset];
    }
    __syncthreads();
}

// interleaved pairs approach to solve warp divergence

// data block unrolling

// warp unrolling

// complete unrolling

// dynamic parallelism

```

unrolling
* loop unrolling: the body of loop is written in code multiple times.
* warp unrolling:
* complete unrolling:


Dynamic Parallelism:
- postpone the decision of exactly how many blocks and grids to create on a GPU until runtime
- make recursive algorithm more transparent and easier to understand
- reduce the need to transfer execution control and data between host and device


# 3. CUDA Memory Model
speed --->
registers   caches    main memory   disk memory
<--- size

Streaming Multiprocessor
- register files
- SMEM
- L1
- constant
- read only

Dynamic Random Access Memory (DRAM)
- L2
- global memory
- texture memory
- constant memory cache


Registers
* fastest memory space in the GPU
* hold frequently accessed thread-private variables and arrays if the indices are constant or can be determined at compile time
* share lifetime with the kernel

Local Memory
* store variables which are eligible for registers but cannot fit into the register space
    - local arrays with indices which cannot resolve at compile time
    - large local structures
* in DRAM, not an on-chip memory, high latency memory access

Shared Memory
* on chip memory which partition among thread blocks __shared__
* L1 cache and shared memory for an SM use the same on-chip memory

GPU ↔ GPU Memory 484GB/s peak bandwidth
GPU ↔ CPU 15.75GB/s (PCIe3)


Pinned Memory
* allocated host memory is by default pageable
* GPU cannot safely access data in pageable host memory
  - when transferring data from pageable host memory to device memory, the cuda drivers first allocate temporary page-locked/pinned memory (host) and copies the host pageable data into that pinned memory. And then transfer that data from pinned memory to device memory.
* cudaMallocHost() directly allocates the pinned memory, cudaFreeHost();

Zero Copy Memory
* pinned memory that is mapped into the device address space 
* both host and device have direct access to that memory
    - leverage host memory when device memory insufficient
    - avoid explicit data transfer
    - improve PCIe transfer rates
* cudaHostAlloc(); cudaFreeHost();

Unified Memory
* creates a pool of managed memory, where each allocation from this memory pool is accessible on CPU and GPU with the same memory address or pointer.
* __device__ __managed__ int y;  cudaMallocManaged();


Memory Access
* aligned memory access
    - first address is an even multiple of the cache granularity
* coalesced memory access
    - 32 threads in a warp access a continuous chunk of memory

Shared Memory
* when memory has to be mis-aligned, non-coalesced
* on-chip memory
* intra-block thread communication channel
* a fixed amount of shared memory is allocated to each thread block when it starts executing.
* Static & Dynamic Shared Memory
  - Static: __shared__ int tile[128];
  - Dynamic: extern __shared__ int tile[];

Bank Conflict
- multiple addresses in a shared memory request fall into the same memory bank
- bank index = (byte address / (4 bytes / bank)) % 32 banks


Constant Memory
* used for data read-only from device and accessed uniformly by threads in a warp
* readable and writable from the host; values in constant memory must be initialized from host
* optimal access pattern:
    - all threads in a warp access the same location
    - access to different addresses by threads within a warp are serialized
* constant memory variables exist for the lifespan of the application and are accessible from all threads within a grid and from the host through runtime functions
* __constant__ cudaMemcpyToSymbol()
* stencil computation


warp shuffle instruction
* allow threads to directly read another thread's register, as long as both threads are in the same warp.
* lower latency than shared memory, no extra memory consumption
* lane: a single thread within a warp; each lane in a warp is uniquely identified by a lane index (0~31)
    - laneID = threadIdx.x % 32
* width: any power of 2 between 2 and 32
    - when set to default warpsize (32), a shuffle instruction is performed across the entire warp and srcLane specifies the laneID of the source thread
    - shuffleID = threadIdx.x % width

[Example]: Reduce

with shared memory

[Example]: Matrix Transpose
out[y * COL + x] = in[x * ROW + y]


with shared memory

with shared memory + padding + unrolling


# 4. CUDA Streams & Events
Grid Level Concurrency: launching multiple kernels to same device simultaneously and overlapping memory transfers with kernel execution

NVVP (NVidia visual profiler) can visualize program executions.

Stream: a sequence of commands that execute in order
- different streams may execute their commands out of order with respect to one another or concurrently
- NULL stream: default stream that kernel launches and data transfers use if not explicitly specify a stream


```cpp
cudaStream_t * stream;
cudaStreamCreate(stream);  // blocking streams
cudaStreamCreateWithFlags();
cudaStreamDestory(stream);

cudaStreamSynchronize(stream);
```

CUDA asynchronous function: cudaMemCpyAsync()

Non-NULL streams are not blocking with respect to the host; operations within a non-NULL stream can be blocked by operations in the NULL stream.


Explicit Synchronization
- synchronize the device cudaDeviceSynchronize();
- synchronize the stream cudaStreamSynchronize();
- synchronize an event in a stream using cudaEventSynchronize();
- synchronize across streams using an event with cudaStreamWaitEvent();

Implicit Synchronization
- page-locked host memory allocation
- device memory allocation, device memort set
- memory copy between two addresses to the same device memory
- any CUDA command to the NULL stream
- switch between L1/shared memory configurations


Event: a marker in a CUDA stream associated with a certain point in the flow of operations in that stream
- synchronize stream execution
- monitor device progress
- measure the execution time of the kernel
```cpp
cudaEventCreate();
cudaEventDestory();
cudaEventRecord();  // queue the event to a CUDA stream
cudaEventSynchronize();
cudaEventQuery();   // check if an event has completed without blocking the host application
cudaEventElapsedTime();
```



CUDA arithmetic instructions
* single/double precision floating point operations
* intrinsic function
* atomic function: perform a mathematical operation, but does so in a single uninterruptable operation with no interference from other threads


IEEE standard 754 
- float   sign (1) + exponent (8) + fraction (23)
- double  sign (1) + exponent (11) + fraction (52)


monolithic kernel: a single large grid of threads to process the entire array in one pass

Grid-Stride Loop
- stride: total number of threads in the grid
- By using a loop with stride equal to the grid size, all addressing within warps is unit-stride, so we get maximum memory coalescing.
```cpp
// kernel loops over the data array one grid-size at a time
__global__ void saxpy(int n, float a, float *x, float *y) {
    for (int i = blockIdx.x * blockDim.x + threadIdx.x; 
        i < n; 
        i += blockDim.x * gridDim.x ) {   
        y[i] = a * x[i] + y[i];
    }
}
```


## 4.1. __restrict__
__restrict__ 类似 volatile

point aliasing

By giving a pointer the restrict property, the programmer is promising the compiler that any data written to through that pointer is not read by any other pointer with the restrict property. 



---

CUDA用作通用计算, Graphics API 只用于显示
GPU架构的缺点: 精度问题; 编程模式不灵活; 
CPU切换线程成本高


CUDA的编程模型将CPU作为主机(Host)，将GPU作为设备(Device)，CPU用来控制整体调度和程序逻辑，GPU负责执行高度线程化的数据并行部分


Latency: 硬件导致的延迟
Thoughput: 吞吐量

CPU: 低延迟, 低吞吐量
    CPU clock: 3GHz
    main Memory latency: ~ 100+ns
    arithmetic instruction latency: ~1+ns
    CPU作为传统处理器，计算核心数较少，每个计算核心有着较高的单核频率，这种结构使CPU擅长于复杂指令调度、分支、逻辑判断和通信等任务。这些任务的逻辑复杂度限制了程序执行的指令并行性

GPU: 高延迟,高吞吐量
    GPU clock: 1GHz
    Memory latency: 300+ns
    arithmetic latency: 10+ns
    GPU的架构与CPU不同，GPU中所说的核，指的是一个流处理器(stream multiprocessor，SM)，每个SM根据GPU型号的不同由若干个标量流处理器(stream processor，SP)组成，SP的功能只有计算。这种架构的优势在于可以容纳上千个没有逻辑关系的数值计算线程进行大量的并行浮点运算，但这种数值运算的并行性在面对逻辑判断执行时却发挥不了优势
GPU非常的IOlimited,所以对与IO要谨慎处理.



Single Instruction, Multiple Data (SIMD)

用SIMD也不是一直是好的.

Streaming Multiprocessor (SM)一般每个有128个single precision CUDA cores(也就是一个线程)和对应的cache.

Block会被分成Warps, Warp是32个线程的集合(都在一个block里面).所有的32线程必须都跑同一组命令集.

一个SM里的Warps是同时跑的.

如果你想用一个Warp做不同的事儿,会按顺序做,也叫Warp Divergence.

warp divergence (1 warp = 32 threads, half warp = 16 threads)


bank conflict 访存串行 (e.g. transpose)
对Nvidia GPUs来说，local memory是由banks组成的，每个bank是32bit，可视化图如下。bank是实际存储单元。每个bank在一次访存中，可以被取址一次。并行访问相同的bank，将导致bank conflicts
CUDA编程中,一个half-warp（16个threads）访问连续的32bit地址,不会有bank conflicts。
一个例外情况是broadcast，如果所有thread访问同一个地址，内存只会被读一次，并broadcast到所有threads



Grid, Block, Thread



```cpp
#include "cuda_runtime.h"

__global__ void hello() {
    int idx = blockDim.x * blockDim.y 
    printf("hi");
}

int main() {
    hello<<< >>>();
}
```




# 5. Memory Hierarchy/Type
I. Global/Device Memory (on host, lifespan the whole grid, 500 cycle latency, no cache)
    memory coalesced = 地址连续 + 开始的地址是每个 thread 所存取的大小的 16 倍
    (1)force align    
    struct __align__(16) vec3d {float x, y, z};    // compiler 在 vec3d 后面加上一个空的 4 bytes，以补齐 16 bytes
    (2)Structure-of-Array, instead of Array-of-Structure
    (3)shared memory, 3-step approach

II. Shared Memory: shared by threads in a block
Bank Conflict: 每个 multiprocessor 有16KB 的 shared memory (以 4 bytes 为单位, 分成16 个 bank)
如果同时每个 thread 是存取不同的 bank, 就不会产生任何问题, 存取 shared memory 的速度和存取寄存器相同; 如果同时有两个(或多个)threads 存取同一个bank 的数据, 就会发生 bank conflict, 这些 threads 就必须照顺序去存取, 而无法同时存取shared memory 了
```cpp
__shared__ int shared_data[128];
```
data[0]是bank 0, data[1]是bank 1, data[2]是bank 2, ..., data[15] 是bank 15, 而 data[16] 又回到bank 0
warp在执行时是以half-warp的方式执行, 因此分属于不同的 half warp 的 threads, 不会造成 bank conflict
```cpp
// 如果程序在存取 shared memory的时候，使用以下的方式: 
int number = shared_data[base + tid];    // 就不会有任何 bank conflict，可以达到最高的效率
// 但是，如果是以下的方式: 
int number = data[base + 4 * tid];
// thread 0 和 thread 4 就会存取到同一个 bank，thread 1 和 thread 5 也是同样，造成 bank conflict。 在这个例子中，一个 half warp 的 16 个 threads 会有四个 threads 存取同一个 bank，因此存取 share memory 的速度会变成原来的1/4

//一个重要的例外是，当多个 thread 存取到同一个 shared memory 的地址时，shared memory 可以将这个地址的 32 bits 数据「广播」到所有读取的 threads，因此不会造成 bank conflict
int number = data[3];   // 不会造成 bank conflict，因为所有的 thread 都读取同一个地址的数据
```

```cpp
// 很多时候 shared memory 的 bank conflict 可以透过修改数据存放的方式来解决
// 例如，以下的程序：
data[tid] = global_data[tid];
... 
int number = shared_data[16 * tid];
// 该程序会造成严重的 bank conflict，为了避免这个问题，可以把数据的排列方式稍加修改，把存取方式改成:
int row = tid / 16;
int column = tid % 16;

data[row * 17 + column] = global_data[tid];
...
int number = shared_data[17 * tid];  这样就不会造成 bank conflict 了
```

Thread同步 __syncthreads();
```cpp
int tid = threadIdx.x;   // thread是第几个thread
int bid = blockIdx.x;    // thread属于第几个block

```


寄存器（register）、共享内存（shared memory）、局部内存（local memory）、常数内存（constant memory）、纹理内存（texture memory）

Video/Device/Global Memory (GPU RAM) 速度和容量直接影响了显卡的性能
从Device Memory拿比从真的RAM快.

- Registers: 最快的,只有线程才能用,生命周期和线程一样
- Local Memory: 150倍慢 (比register和shared memory)
- Shared Memory: 当没有bank conflicts或者从同一个地址读的时候, 可以和register一样快. 对于一个block里面的所有线程都可见. 和block一样的生命周期
- Global/Device Memory: 150倍慢 (比register和shared memory)

Cache
- 每个Streaming Multiprocessor拥有自己的L1缓存 (L1-cache)， 所有的SM共同使用L2缓存




# 6. Pytorch
PyTorch的的代码主要由C10、ATen、torch三大部分组成的

- C10，来自于Caffe Tensor Library的缩写。这里存放的都是最基础的Tensor库的代码，可以运行在服务端和移动端。PyTorch目前正在将代码从ATen/core目录下迁移到C10中。C10的代码有一些特殊性，体现在这里的代码除了服务端外还要运行在移动端，因此编译后的二进制文件大小也很关键，因此C10目前存放的都是最核心、精简的、基础的Tensor函数和接口。
- ATen，来自于 A TENsor library for C++11的缩写；PyTorch的C++ tensor library。ATen部分有大量的代码是来声明和定义Tensor运算相关的逻辑的，除此之外，PyTorch还使用了aten/src/ATen/gen.py来动态生成一些ATen相关的代码
- Torch，部分代码仍然在使用以前的快要进入历史博物馆的Torch开源项目



# 7. TensorRT

TensorRT Optimization:
- precision calibration
- kernel auto-tuning
- layer & tensor fusion (Conv + Bias + Relu → CBR)
- multi-stream execution
- dynamic tensor memory


Procedure:
- builder
- network
- API or parser network

Dynamic Shape (since TensorRT6.0)

TensorRT Plugin

Quantization
FP16 和 INT8能加速的本质: 通过指令 或 硬件技术, 在单位时钟周期内, FP16 和 INT8 类型的运算次数 大于 FP32 类型的运算次数


# 8. Examples

Reduction

矩阵乘法


SAXY

矩阵取逆

滤波


软光栅

Mesh 

三角形 
Vertex (X, Y, Z) 线性表
Face (V1, V2, V3) 


Viewing Cone 视锥, 确定那些

Z-buffer (depth 深度)

锯齿边缘(Jagged Edges)的产生和光栅器将顶点数据转化为片段的方式有关

走样(Aliasing): 清楚看见形成边缘的像素
抗锯齿/反走样 (Anti-Aliasing): 缓解这种现象，从而产生更平滑的边缘

- 超采样抗锯齿(Super Sample Anti-aliasing, SSAA), 使用比正常分辨率更高的分辨率(超采样)来渲染场景，当图像输出在帧缓冲中更新时，分辨率会被下采样(Downsample)至正常的分辨率。这些额外的分辨率会被用来防止锯齿边缘的产生。虽然能够解决走样的问题，但是比平时要绘制更多的片段，会带来很大的性能开销
- 多重采样抗锯齿(Multisample Anti-aliasing, MSAA), 借鉴了SSAA背后的理念，但却以更加高效的方式实现了抗锯齿

光栅器是位于最终处理过的顶点之后到片段着色器之前所经过的所有的算法与过程的总和。光栅器会将一个图元的所有顶点作为输入，并将它转换为一系列的片段。顶点坐标理论上可以取任意值，但片段不行，因为它们受限于你窗口的分辨率。顶点坐标与片段之间几乎永远也不会有一对一的映射，所以光栅器必须以某种方式来决定每个顶点最终所在的片段/屏幕坐标。


https://learnopengl.com/Advanced-OpenGL/Anti-Aliasing



常用的优化方法
（线程束->线程块）对于block和thread的分配问题，有这么一个技巧，每个block里面的thread个数最好是32的倍数，因为，这样可以让线程束一起执行，计算效率更高，促进memory coalescing
（ 线程块 ）一个sm只会执行一个block里的warp，当该block里warp执行完才会执行其他block里的warp。进行划分时，最好保证每个block里的warp比较合理，那样可以一个sm可以交替执行里面的warp，从而提高效率，此外，在分配block时，要根据GPU的sm个数，分配出合理的block数，让GPU的sm都利用起来，提利用率。分配时，也要考虑到同一个线程block的资源问题，不要出现对应的资源不够。
（内存）共享内存的使用量也是影响occupancy的一个重要因子，一块大核拥有一块共享内存。shared添加到变量声明中，这将使这个变量驻留在共享内存中。在声明共享内存变量后，线程块中的每个线程都共享这块内存，使得一个线程块中的多个线程能够在计算上进行通信和协作。
（内存）纹理缓存是只读的内存，专门为内存访问存在大量空间局部性的设计，核函数需要特殊的函数告诉GPU读取纹理内存而不是全局内存。使用纹理内存，如果同一个线程束内的thread的访问地址很近的话，那么性能更高。