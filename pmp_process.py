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
    pass

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
