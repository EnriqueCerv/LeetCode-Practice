def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = ' '.join(s.split())
        spaces = [-1]
        for i in range(len(s)):
            if s[i] == ' ':
                spaces.append(i)
        spaces.append(len(s))
        print(s, spaces)

        s_out = ''
        for i in reversed(range(len(spaces)-1)):
            s_out += s[spaces[i]+1:spaces[i+1]]
            s_out += ' '
        return s_out.strip()

def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])