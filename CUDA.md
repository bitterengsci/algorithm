
char 1 byte = 8 bits
int 4 bytes
float 4 bytes


# CUDA
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


## Grid, Block, Thread
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

## Memory Transfer
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

## Error Handling
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

## Device Properties
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

# CUDA Execution Model
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


# CUDA Memory Model
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


# CUDA Streams & Events
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

---

CUDA用作通用计算, Graphics API 只用于显示
GPU架构的缺点: 精度问题; 编程模式不灵活; 
CPU切换线程成本高


CUDA的编程模型将CPU作为主机(Host)，将GPU作为设备(Device)，CPU用来控制整体调度和程序逻辑，GPU负责执行高度线程化的数据并行部分




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




Memory Hierarchy
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