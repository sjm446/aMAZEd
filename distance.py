"""
Distance computation in a maze

MIT License

Copyright (c) 2017 Gaurav Mathur

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

class Distances:
    """ This object holds information on the distance of all the cells from 
    this cell. 'self.root' holds the reference to this cell. 
    """
    def __init__(self, root):
        self.root = root
        self.cells = dict()
        self.cells[root] = 0

    def __getitem__(self, cell):
        """ Overloaded indexing operation on this object """
        return self.cells[cell] if cell in self.cells else None

    def __setitem__(self, cell, distance):
        """ Overloading set via indexing on this object """
        self.cells[cell] = distance

    def show(self):
        for cell in self.cells:
            print(cell, self.cells[cell])

    def get_cells(self):
        return self.cells.keys()

