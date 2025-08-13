# Last updated: 13.08.2025, 17:00:22
class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path = path.split('/')
        ans = []

        for item in new_path:
            if item in ('', '.'):
                continue

            elif item == '..':
                if ans:
                    ans.pop()
            
            else:
                ans.append(item)

        if not ans:
            return '/'

        return '/' + '/'.join(ans)
        