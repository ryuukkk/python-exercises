def indented_list_sort(indented_list, indent = '    '):
    KEY, ITEM, CHILDREN = range(3)


    '''add_entry method adds items to an entries list that stores 3-tuples for each item in 
    the indented_list that we need to sort. The 3-tuples are of form (key, item, children);
    key is used for sorting, item is the actual value, children is a list similar to entries that
    stores item starting with next indent.'''
    def add_entry(level, key, item, children):
        if level==0:
            children.append((key, item, []))
        else:
            add_entry(level-1, key, item, children[-1][CHILDREN])
    
    '''add each entry in entries list, sorted by key, to the final list'''
    def update_indented_list(entry):
        indented_list.append(entry[ITEM])
        for subentry in sorted(entry[CHILDREN]):
            update_indented_list(subentry)
        
    entries = []
    for item in indented_list:
        level = 0
        i = 0
        while item.startswith(indent, i):
            i += len(indent)
            level+=1
        key = item.strip().lower()
        add_entry(level, key, item, entries)
    
    indented_list = []
    for entry in sorted(entries):
        update_indented_list(entry)
    
    return indented_list

if __name__ == '__main__':
    before =  ["Nonmetals", 
              "    Hydrogen", 
              "    Carbon", 
              "    Nitrogen", 
              "    Oxygen", 
              "Inner Transitionals", 
              "    Lanthanides", 
              "        Cerium", 
              "        Europium", 
              "    Actinides", 
              "        Uranium", 
              "        Curium", 
              "        Plutonium", 
              "Alkali Metals", 
              "    Lithium", 
              "    Sodium", 
              "    Potassium"]
    
    for item in indented_list_sort(before):
        print(item)
    
