# We will use a file-sharing system to share a very large file which consists of m small chunks with IDs from 1 to m.

# When users join the system, the system should assign a unique ID to them. The unique ID should be used once for each user, but when a user leaves the system, the ID can be reused again.

# Users can request a certain chunk of the file, the system should return a list of IDs of all the users who own this chunk. If the user receives a non-empty list of IDs, they receive the requested chunk successfully.


# Implement the FileSharing class:

# FileSharing(int m) Initializes the object with a file of m chunks.
# int join(int[] ownedChunks): A new user joined the system owning some chunks of the file, the system should assign an id to the user which is the smallest positive integer not taken by any other user. Return the assigned id.
# void leave(int userID): The user with userID will leave the system, you cannot take file chunks from them anymore.
# int[] request(int userID, int chunkID): The user userID requested the file chunk with chunkID. Return a list of the IDs of all users that own this chunk sorted in ascending order.


# From discussion
# For those struggling with why their solution isn't working: the statement, "If the user receives a non-empty list of IDs, they receive the requested chunk successfully", requires further explanation. Essentially, when a user requests a chunk, if any other user already owns that chunk, the requesting user will also be considered an owner of that chunk in subsequent requests. However, in this specific request, the userID should not be included in the return list. On the other hand, if no user currently owns the chunk, an empty list will be returned, indicating that the requesting user has failed to acquire the chunk.


import heapq
from typing import List


class FileSharing:

    def __init__(self, m: int):
        self.dct = {}
        self.id = 1
        self.available_ids = []

    def join(self, ownedChunks: List[int]) -> int:

        if self.available_ids:
            new_id = heapq.heappop(self.available_ids)
            self.dct[new_id] = set(ownedChunks)
            return new_id
        
        self.dct[self.id] = set(ownedChunks)
        current_id = self.id
        self.id += 1

        return current_id

    def leave(self, userID: int) -> None:
        del self.dct[userID]
        heapq.heappush(self.available_ids, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:

        result = []
        for user, chunk_list in self.dct.items():
            if (chunkID in chunk_list):
                result.append(user)
        if result:
            self.dct[userID].add(chunkID)

        return sorted(result)


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)


fileSharing = FileSharing(4)
print(fileSharing.join([1, 2]))
print(fileSharing.join([2, 3]))
print(fileSharing.join([4]))
print(fileSharing.request(1, 3))
print(fileSharing.request(2, 2))
print(fileSharing.leave(1))
print(fileSharing.request(2, 1))
print(fileSharing.leave(2))
print(fileSharing.join([]))

# Example:

# Input:
# ["FileSharing","join","join","join","request","request","leave","request","leave","join"]
# [[4],[[1,2]],[[2,3]],[[4]],[1,3],[2,2],[1],[2,1],[2],[[]]]
# Output:
# [null,1,2,3,[2],[1,2],null,[],null,1]
# Explanation:
# FileSharing fileSharing = new FileSharing(4); // We use the system to share a file of 4 chunks.
# fileSharing.join([1, 2]);    // A user who has chunks [1,2] joined the system, assign id = 1 to them and return 1.
# fileSharing.join([2, 3]);    // A user who has chunks [2,3] joined the system, assign id = 2 to them and return 2.
# fileSharing.join([4]);       // A user who has chunk [4] joined the system, assign id = 3 to them and return 3.
# fileSharing.request(1, 3);   // The user with id = 1 requested the third file chunk, as only the user with id = 2 has the file, return [2] . Notice that user 1 now has chunks [1,2,3].
# fileSharing.request(2, 2);   // The user with id = 2 requested the second file chunk, users with ids [1,2] have this chunk, thus we return [1,2].
# fileSharing.leave(1);        // The user with id = 1 left the system, all the file chunks with them are no longer available for other users.
# fileSharing.request(2, 1);   // The user with id = 2 requested the first file chunk, no one in the system has this chunk, we return empty list [].
# fileSharing.leave(2);        // The user with id = 2 left the system.
# fileSharing.join([]);        // A user who doesn't have any chunks joined the system, assign id = 1 to them and return 1. Notice that ids 1 and 2 are free and we can reuse them.
