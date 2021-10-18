class Solution:
    def numUniqueEmails(self, emails) :
        
        uniqueMails = set()
        
        for email in emails:
            localName =""
            for currChar in email:
                if currChar == '+' or currChar == '@':
                    break
                elif currChar =='.':
                    continue
                localName += currChar
            domainName = ""
            
            lenEmail = len(email)-1
            
            for charIndex in range(lenEmail, -1, -1):
                if email[charIndex] == '@':
                    break
                domainName += email[charIndex]
            
            uniqueMails.add(localName +'@'+ domainName[::-1])
        return len(uniqueMails)
