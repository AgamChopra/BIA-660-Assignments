#Agamdeep S Chopra
#HW 1
#BIA 660, Spring 2021
#Score: 13/10

import string

def tokenize(text):
    
    cleaned_tokens = []
    cleaned_tokens = [text.split()[i].strip(string.punctuation).lower() for i in range(len(text.split())) if len(text.split()[i])>1]
    
    return cleaned_tokens

class Text_Analyzer(object):
    
    def __init__(self, doc):
        self.text = doc
        self.token_count = {}
        
    def analyze(self):
        temp={}
        temp = tokenize(self.text)
        for i in range(len(temp)):
            if temp[i] in self.token_count:
                self.token_count[temp[i]] += 1
            else:
                self.token_count[temp[i]] = 1
        return self.token_count
        
    def topN(self, N):
        temp_dict = {}
        temp_dict = sorted(self.token_count.items(), key=lambda x: x[-1])
        return [temp_dict[-1-i] for i in range(N)]

class Text_Analyzer(object):
    
    def __init__(self, doc):
        self.text = doc
        self.token_count = {}
        
    def analyze(self):
        temp={}
        temp = tokenize(self.text)
        for i in range(len(temp)):
            if temp[i] in self.token_count:
                self.token_count[temp[i]] += 1
            else:
                self.token_count[temp[i]] = 1
        return self.token_count
        
    def topN(self, N):
        temp_dict = {}
        temp_dict = sorted(self.token_count.items(), key=lambda x: x[-1])
        return [temp_dict[-1-i] for i in range(N)]
    
    def bigram(self, N):
        temp_dict = {}
        bi_dict = []
        token_count = tokenize(self.text)
        #print(token_count)
        for i in range(len(token_count) - 1):
            bi_dict.append(token_count[i:i+2])
        #print(str(bi_dict[2]))
        for i in range(len(bi_dict)):
            if str(bi_dict[i]) in temp_dict:
                temp_dict[str(bi_dict[i])] += 1
            else:
                temp_dict[str(bi_dict[i])] = 1
        temp_dict = sorted(temp_dict.items(), key=lambda x: x[-1])
        return [temp_dict[-1-i] for i in range(N)]

if __name__ == "__main__":  
    
    # Test Question 1
    text='''What does "immunity" really mean?
            To scientists, immunity means a resistance to a disease gained 
            through the immune system’s exposure to it, either by infection 
            or through vaccination. But immunity doesn’t always mean complete 
            protection from the virus. 

            How does the body build immunity?
            The immune system has two ways to provide lasting protection: 
            T cells that remember the pathogen and trigger a rapid response, 
            and B cells that produce antibodies — proteins the body makes 
            to fight off a specific pathogen.
            So-called “memory T cells” also stick around. Ideally, they live up 
            to their name and recognize a previously encountered pathogen 
            and either help coordinate the immune system or kill infected cells. 
        ''' 
    print("Test Question 1")
    print(tokenize(text))
    
    
    # Test Question 2
    print("\nTest Question 2")
    analyzer=Text_Analyzer(text)
    analyzer.analyze()
    print(analyzer.token_count)
    print(analyzer.topN(5))
    
    
    #3 Test Question 3
    print("\nTest Question 3")
    print(analyzer.bigram(3))
    
    print("\nQ2 Analysis:\nIt appears that filler words such as is, and, a, etc tend to be the most frequent inn normal english sentences.\n\nQ3 Analysis:\n Immune System was an interesting biagram that I found in the test case below.")