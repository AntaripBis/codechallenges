"""
I have used recursion and trie to solve the problem
"""
import time
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self._create_node()
        self.a_ord = ord("a")

    def _create_node(self,is_end_of_word=False):
        return {"children":[None]*26,"is_end_of_word":is_end_of_word}
    
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if word is None or len(word) == 0:
            return
        current_node = self.root
        for i in range(len(word)):
            idx =  ord(word[i]) - self.a_ord
            temp_node = current_node["children"][idx]
            if temp_node is None:
                temp_node = self._create_node()
                current_node["children"][idx] = temp_node
            current_node = temp_node
        current_node["is_end_of_word"] = True
            
           

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) == 0:
            return False
        current_node = self.root
        for character in word:
            idx =  ord(character) - self.a_ord
            if current_node["children"][idx] is None:
                return False
            current_node = current_node["children"][idx]
        
        return current_node["is_end_of_word"]
            
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix is None or len(prefix) == 0:
            return False
        current_node = self.root
        for character in prefix:
            idx =  ord(character) - self.a_ord
            if current_node["children"][idx] is None:
                return False
            current_node = current_node["children"][idx]
            
        
        return True

        


class Solution:
    
    def _generate_word_trie(self,words):
        self.word_trie = Trie()
        for word in words:
            if not self.word_trie.search(word):
                self.word_trie.insert(word)
			
    def _check_strings_at_node(self,node_idx,path_str,node_idx_list,board):
        if len(self.word_set) == 0:
            return
        
        #print("New node dimension :: ")
        #print(node_idx)
        #print("Path string :: "+path_str)
        temp_str = path_str+board[node_idx[0]][node_idx[1]]
        #print("Temp string :: "+temp_str)
        if temp_str in self.forbidden_prefix_set:
            return 
        elif not self.word_trie.startsWith(temp_str):
            self.forbidden_prefix_set.add(temp_str)
            return

        if self.word_trie.search(temp_str) and temp_str in self.word_set:
            #print("Complete word found :: "+temp_str)
            self.word_set.remove(temp_str)
            self.words_present.append(temp_str)
            if len(self.word_set) == 0:
                return
        
        node_idx_list.append(node_idx)
        node_idx_set = set(node_idx_list)
        if node_idx[1] < len(board[node_idx[0]])-1 and (node_idx[0],node_idx[1]+1) not in node_idx_set:
            self._check_strings_at_node((node_idx[0],node_idx[1]+1),temp_str,node_idx_list.copy(),board)
        if node_idx[0] > 0 and (node_idx[0]-1,node_idx[1]) not in node_idx_set:
            self._check_strings_at_node((node_idx[0]-1,node_idx[1]),temp_str,node_idx_list.copy(),board)
        if node_idx[1] > 0 and (node_idx[0],node_idx[1]-1) not in node_idx_set:
            self._check_strings_at_node((node_idx[0],node_idx[1]-1),temp_str,node_idx_list.copy(),board)
        if node_idx[0] < len(board)-1 and (node_idx[0]+1,node_idx[1]) not in node_idx_set:
            self._check_strings_at_node((node_idx[0]+1,node_idx[1]),temp_str,node_idx_list.copy(),board)
            
        #print("All possibilities completed at these level")
        #print("="*50)
            
        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0 or len(board) == 0:
            return []
        
        if len(words) > 30:
            board_set = set(board[0])
            #print("Board set :: "+str(board_set))
            for i in range(1,len(board)):
                for char in board[i]:
                    board_set.add(char)
            words = [word for word in words if word[0] in board_set]
        
        self.word_set = set(words) if len(words) > 1 else {words[0]}
        self._generate_word_trie(self.word_set)
        self.forbidden_prefix_set = set()
        '''
        print("Word set initially ::")
        print(word_set)
        '''
        self.words_present = list()
        for i in range(len(board)):
            for j in range(len(board[i])):
                '''
                print("Dimension of the start state")
                print(str((i,j)))
                '''
                self._check_strings_at_node((i,j),"",list(),board)
                if len(self.word_set) == 0:
                    return self.words_present
                '''
                print("Start state completed")
                print("="*50)
                '''
               
        return self.words_present
                
