class pmp_object(object):
    def __init__(self, name):
        self.name=name
        self.up_set=set([])
        self.down_set=set([])
    
    def add(self, pmp_type, obj):
        if ((pmp_type=="up") or (pmp_type=="in")):
            self.up_set.add(obj)
        elif ((pmp_type=="down") or (pmp_type="out")):
            self.down_set.add(obj)
        else:
            print ("pmp_type error: " % pmp_type)

def read_from_file(file_name, proc_dict, file_dict):
    proc_name = ''
    with open( file_name, 'r' ) as f:
        for line in f:
            if ('[process]' in line):
                proc_name=line.replace('[process]','')
                if not (proc_name in proc_dict.keys()):
                    proc_dict[proc_name]=pmp_object(proc_name)
            elif ('[input]' in line):
                input_files=line.replace('[input]','').split(';')
                for in_file in input_files:
                    if not (in_file in file_dict.keys()):
                        file_dict[in_file]=pmp_object(in_file)
                    proc_dict[proc_name].add('in',file_dict[in_file])
                    file_dict[in_file].add('down',proc_dict[proc_name])
            elif ('[output]' in line):
                output_files=line.replace('[output]','').split(';')
                for out_file in output_files:
                    if not (out_file in file_dict.keys()):
                        file_dict[out_file]=pmp_object(out_file)
                    proc_dict[proc_name].add('out',file_dict[out_file])
                    file_dict[out_file].add('up',proc_dict[proc_name])
            else:
                proc_name=''

def go_through_proc(first_proc, proc_dict):
    pass

def main():
    process_dict=dict()
    file_dict=dict()

    read_from_file(file_name, process_dict, file_dict)

    if (INIT_PROC_NAME in process_dict.keys()):
        go_through_proc(process_dict[INIT_PROC_NAME], process_dict)
    else:
        print("error in reading process, no initial process found")

if __name__ == '__main__':
    main()
