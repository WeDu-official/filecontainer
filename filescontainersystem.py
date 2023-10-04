class filecontainer():
    def __init__(self):
        pass
    def find_between(self,code:str,first_word:str, second_word:str, occurrence:int):
        lines = code.strip().split("\n")
        first_line_number = None
        second_line_number = None
        count = 0

        for i, line in enumerate(lines):
            if first_word in line:
                count += 1
                if count == occurrence:
                    first_line_number = i
            if second_word in line and count == occurrence:
                second_line_number = i
                break

        if first_line_number is not None and second_line_number is not None:
            words_between = []
            for i in range(first_line_number + 1, second_line_number):
                line = lines[i].strip()
                words_between.append(lines[i])
            return words_between
        else:
            return []  # If either first_word or second_word is not found in the file or occurrence is not found
    def list_to_string(self,lst):
        string = '\n'.join(lst)
        return string.replace(r'\\n',r'\n')
    def makeplankFC(self,filepath,filename):
        if filepath != '':
            x = open(f'{filepath}{filename}.fc','x')
            x.close()
        else:
            x2 = open(f'{filename}.fc','x')
            x2.close()
    def FCmaker(self,file_path:str,filespathop_list:list,localpathslist:list):
        self.filepath = file_path
        self.fileslist = filespathop_list
        self.i = 0
        self.delfile = open(self.filepath, 'w')
        self.delfile.write('')
        self.delfile.close()
        for i2 in range(len(self.fileslist)):
            self._extracted_from_FCmaker_9(i2, localpathslist)
    def _extracted_from_FCmaker_9(self, i2, localpathslist):
        self.i += 1
        self.makefilechank = f'''<s>{self.i}\n{open(self.fileslist[i2],'r').read()}\n<e>{self.i}\n'''
        self.makepathchank = f'''<s path>{self.i}\n{localpathslist[i2]}\n<e path>{self.i}\n'''
        self.writingfile = open(self.filepath,'a')
        print(self.makefilechank, file=self.writingfile)
        print(self.makepathchank, file=self.writingfile)
        self.writingfile.close()
    def edit_line(self, file_name, line_number, new_text):
        """Edits the specified line in the given Python file.

        Args:
          file_name: The name of the Python file to edit.
          line_number: The number of the line to edit.
          new_text: The new text to write to the file.
        """

        with open(file_name, "r") as f:
            source_code = f.read()

        lines = source_code.split("\n")
        lines[line_number - 1] = new_text

        with open(file_name, "w") as f:
            f.write("\n".join(lines))
    def FCopener(self,file_path:str):
        self.readingfile = open(file_path, 'r')
        self.readedfile = self.readingfile.read()
        self.readingfile.close()
        for i in range(1000):
            self.filecode:str = self.list_to_string(self.find_between(self.readedfile,f'<s>{i}',f'<e>{i}',1))
            self.ourlocalfilespath:str = self.list_to_string(self.find_between(self.readedfile, f'<s path>{i}', f'<e path>{i}', 1))
            if self.ourlocalfilespath not in ['', ' ']:
                try:
                    pross1 = open(f'{self.ourlocalfilespath}', 'x')
                    pross1.close()
                    with open(f'{self.ourlocalfilespath}', 'a') as pross2:
                        print(self.filecode,file=pross2)
                except FileExistsError:
                    print('''Error:file exists or something else that means their is file that have
                the same and file format of another file found in the extract place.''')
FC = filecontainer()