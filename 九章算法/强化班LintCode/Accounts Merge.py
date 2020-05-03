'''
1070. Accounts Merge
Given a list accounts, each element accounts[i] is a list of strings, 
where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. 
Two accounts definitely belong to the same person if there is some email that is common to both accounts. 
Note that even if two accounts have the same name, 
they may belong to different people as people could have the same name. 
A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: 
the first element of each account is the name, and the rest of the elements are emails in sorted order. 
The accounts themselves can be returned in any order.

Example:
	Input:
	[
		["John", "johnsmith@mail.com", "john00@mail.com"],
		["John", "johnnybravo@mail.com"],
		["John", "johnsmith@mail.com", "john_newyork@mail.com"],
		["Mary", "mary@mail.com"]
	]
	
	Output: 
	[
		["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
		["John", "johnnybravo@mail.com"],
		["Mary", "mary@mail.com"]
	]

	Explanation: 
	    The first and third John's are the same person as they have the common email "johnsmith@mail.com".
	    The second John and Mary are different people as none of their email addresses are used by other accounts.

	You could return these lists in any order, for example the answer
	[
		['Mary', 'mary@mail.com'],
		['John', 'johnnybravo@mail.com'],
		['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
	]
    is also acceptable.

'''


class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        # initialization
        self.father = {}
        for i in range(len(accounts)):
            self.father[i] = i
        email_to_ids = self.get_email_to_ids(accounts)
        
        # union
        for email, ids in email_to_ids.items():
            root_id = ids[0]
            for id in ids[1:]:
                self.union(id, root_id)
                
        id_to_email_set = self.get_id_to_email_set(accounts)
        
        merged_accounts = []
        for user_id, email_set in id_to_email_set.items():
            merged_accounts.append([accounts[user_id][0],*sorted(email_set)])
            
        return merged_accounts
    
    def get_id_to_email_set(self, accounts):
        id_to_email_set = {}
        for user_id, account in enumerate(accounts):
            root_user_id = self.find(user_id)
            email_set = id_to_email_set.get(root_user_id, set())
            for email in account[1:]:
                email_set.add(email)
            id_to_email_set[root_user_id] = email_set
        return id_to_email_set
            
    def get_email_to_ids(self, accounts):
        email_to_ids = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_ids[email] = email_to_ids.get(email, [])
                email_to_ids[email].append(i)
        return email_to_ids
        
    def union(self, id1, id2):
        self.father[self.find(id1)] = self.find(id2)

    def find(self, user_id):
        path = []
        while user_id != self.father[user_id]:
            path.append(user_id)
            user_id = self.father[user_id]
            
        for u in path:
            self.father[u] = user_id
            
        return user_id