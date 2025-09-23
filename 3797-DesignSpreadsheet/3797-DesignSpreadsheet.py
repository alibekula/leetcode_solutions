# Last updated: 23.09.2025, 16:40:11
class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {chr(ord('A') + key): dict() for key in range(0, 26)}

    def setCell(self, cell: str, value: int) -> None:
        char, num = cell[0], cell[1:]
        self.sheet[char][num] = value
        

    def resetCell(self, cell: str) -> None:
        char, num = cell[0], cell[1:]
        self.sheet[char][num] = 0 
        
    def getValue(self, formula: str) -> int:
        val1, val2 = formula.lstrip('=').split('+')

        val1 = int(val1) if val1.isdigit() else self.sheet[val1[0]].get(val1[1:], 0)
        val2 = int(val2) if val2.isdigit() else self.sheet[val2[0]].get(val2[1:], 0)

        return val1 + val2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)