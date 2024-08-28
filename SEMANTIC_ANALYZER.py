mainTable_ = []
functionTable_ = []
extraTable_=[]
MainTable_=[]
scopeStack_ = [0]
highestScope = 0
typeCompatibility = {
    "intint+": "int",
    "intint-": "int",
    "intint*": "int",
    "intint/": "int",
    "intint%": "int",
    "intint=": "int",
    "intint==": " bool",
    "intint!=": "bool",
    "intint<=": "bool",
    "intint<": "bool",
    "intint>": "bool",
    "intint>=": "bool",
    "intfloat+": "float",
    "intfloat-": "float",
    "intfloat*": "float",
    "intfloat/": "float",
    "intfloat=": "int",
    "intfloat==": "bool",
    "intfloat!=": "bool",
    "intfloat<=": "bool",
    "intfloat<": "bool",
    "intfloat>": "bool",
    "intfloat>=": "bool",
    "intchar+": "int",
    "intchar-": "int",
    "intchar*": "int",
    "intchar/": "int",
    "intchar%": "int",
    "intchar=": "int",
    "intchar==": "bool",
    "intchar!=": "bool",
    "intchar<=": "bool",
    "intchar<": "bool",
    "intchar>": "bool",
    "intchar>=": "bool",
    "intbool+": "int",
    "intbool-": "int",
    "intbool*": "int",
    "intbool/": "int",
    "intbool%": "int",
    "intbool=": "int",
    "intbool==":  "bool",
    "intbool!=": "bool",
    "intbool<=": "bool",
    "intbool<": "bool",
    "intbool>": "bool",
    "intbool>=": "bool",
    "floatfloat+": "float",
    "floatfloat-": "float",
    "floatfloat*": "float",
    "floatfloat/": "float",
    "floatfloat=": "float",
    "floatfloat==": "bool",
    "floatfloat!=": "bool",
    "floatfloat<=": "bool",
    "floatfloat<": "bool",
    "floatfloat>": "bool",
    "floatfloat>=": "bool",
    "floatchar+": "float",
    "floatchar-": "float",
    "floatchar*": "float",
    "floatchar/": "float",
    "floatchar%": "float",
    "floatchar=": "float",
    "floatchar==": "bool",
    "floatchar!=": "bool",
    "floatchar<=": "bool",
    "floatchar<": "bool",
    "floatchar>": "bool",
    "floatchar>=": "bool",
    "floatbool+": "float",
    "floatbool-": "float",
    "floatbool*": "float",
    "floatbool/": "float",
    "floatbool=": "bool",
    "floatbool==": "bool",
    "floatbool!=": "bool",
    "floatbool<=": "bool",
    "floatbool<": "bool",
    "floatbool>": "bool",
    "floatbool>=": "bool",
    "stringstring+": "string",
    "stringstring=":  "string",
    "stringstring==": "bool",
    "stringstring!=": "bool",
    "stringstring<=": "bool",
    "stringstring<": "bool",
    "stringstring>": "bool",
    "stringstring>=": "bool",
    "stringint=": "int",
    "stringfloat=": "int",
    "stringchar+": "string",
    "stringchar=": "string",
    "stringbool=": "string",
    "charchar+": "int",
    "charchar-": "int",
    "charchar*": "int",
    "charchar/": "int",
    "charchar%": "int",
    "charchar=": "char",
    "charchar==": "bool",
    "charchar!=": "bool",
    "charchar<=": "bool",
    "charchar<": "bool",
    "charchar>": "bool",
    "charchar>=": "bool",
    "charint+": "char",
    "charint-": "char",
    "charint*": "char",
    "charint/": "char",
    "charint%": "int",
    "charint=": "char",
    "charint==": "bool",
    "charint!=": "bool",
    "charint<=": "bool",
    "charint<": "bool",
    "charint>": "bool",
    "charint>=": "bool",
    "charfloat+": "float",
    "charfloat-": "float",
    "charfloat*": "float",
    "charfloat/": "float",
    "charfloat=": "char",
    "charfloat==": "bool",
    "charfloat!=": "bool",
    "charfloat<=": "bool",
    "charfloat<": "bool",
    "charfloat>": "bool",
    "charfloat>=": "bool",
    "charstring+": "string",
    "charbool+":  "int",
    "charbool-": "int",
    "charbool*": "int",
    "charbool/": "int",
    "charbool%": "int",
    "charbool=": "char",
    "charbool==": "bool",
    "charbool!=": "bool",
    "charbool<=": "bool",
    "charbool<": "bool",
    "charbool>": "bool",
    "charbool>=": "bool",
    "boolbool+": "bool",
    "boolbool-": "bool",
    "boolbool*": "bool",
    "boolbool/": "bool",
    "boolbool%": "bool",
    "boolbool=": "bool",
    "boolbool==": "bool",
    "boolbool!=": "bool",
    "boolbool<=": "bool",
    "boolbool<": "bool",
    "boolbool>": "bool",
    "boolbool>=": "bool",
    "boolbool&&": "bool",
    "boolbool||": "bool",
    "boolint+": "int",
    "boolint-": "int",
    "boolint*": "int",
    "boolint/": "int",
    "boolint%": "int",
    "boolint=": "bool",
    "boolint==": "bool",
    "boolint!=": "bool",
    "boolint<=": "bool",
    "boolint<": "bool",
    "boolint>": "bool",
    "boolint>=": "bool",
    "boolfloat-": "float",
    "boolfloat*": "float",
    "boolfloat/": "float",
    "boolfloat%": "float",
    "boolfloat=": "bool",
    "boolfloat==": "bool",
    "boolfloat!=": "bool",
    "boolfloat<=": "bool",
    "boolfloat<": "bool",
    "boolfloat>": "bool",
    "boolfloat>=": "bool",
    "boolchar+": "int",
    "boolchar-": "int",
    "boolchar*": "int",
    "boolchar/": "int",
    "boolchar%": "int",
    "boolchar=": "bool",
    "boolchar==": "bool",
    "boolchar!=": "bool",
    "boolchar<=": "bool",
    "boolchar<": "bool",
    "boolchar>": "bool",
    "boolchar>=": "bool",
    "char!": "bool",
    "int!": "bool",
    "int++": "int",
    "int--": "int",
    "float!": "bool",
    # "bool!": "bool",
    # "bool++": "bool",
    # "bool--": "bool",
    # "char++": "char",
    # "char--": "char",
    # "float++": "float",
    # "float--": "float"
}


# class mainTable:
class DefinitionTable:
    def __init__(self, name, Type, typeMod, parent):
        self.name = name
        self.type = Type
        self.typeMod = typeMod
        self.parent = parent
        self.attrTable = []


# class attributeTable:
class MemberTable:
    def __init__(self, name, params, Type, accessMod, stat, concCond):
        self.name = name
        self.params = params
        self.type = Type
        self.accessMod = accessMod
        self.stat = stat
        self.concCond = concCond


# class functionTable:
class ScopeTable:
    def __init__(self, name, Type, scope):
        self.name = name
        self.type = Type
        self.scope = scope


# def lookupMainTable(name):
def lookupDefinitionTable(name):
    x = next((j for j in mainTable_ if j.name == name), "")
    if (x == ""):
        return False
    # print("\tLookUp Main Table")
    # print(vars(x))
    return x


# def insertMainTable(name, ofType, typeMod, parent):
def insertDefinitionTable(name, Type, typeMod, parent):
    if (lookupDefinitionTable(name) == False):
        obj = DefinitionTable(name, Type, typeMod, parent)
        mainTable_.append(obj)
        # print("\tMain Table")
        # for t in mainTable_:
        #     print(vars(t))
        return True
    print("CLASS REDECLARATION --->", Type , name )
    return False

def InsertDefinitionTable(name, Type, typeMod, parent):
    if (lookupDefinitionTable(name) == False):
        obj = DefinitionTable(name, Type, typeMod, parent)
        MainTable_.append(obj)
        # print("\tMain Table")
        # for t in mainTable_:
        #     print(vars(t))
        return True
    # print("CLASS REDECLARATION --->", Type , name )
    return False
# name = "A"
# type = "class"
# TM = None
# parent = None 
# insertDefinitionTable(name , type , TM , parent)

# for obj in mainTable_:
#     print(vars(obj))

# def lookupAttributeTable(name, paramList, ofName):
def lookupMemberTable(name, paramList, ofName):
    x = lookupDefinitionTable(ofName)
    if (x != False):
        if (paramList == "~"):
            y = next((j for j in x.attrTable if j.name == name), "")
            if (y == ""):
                return False
            # print("\tLookUp Attr Table")
            # print(vars(y))
            return y
        else:
            y = next((j for j in x.attrTable if j.name ==
                     name and j.params == paramList), "")
            if (y == ""):
                return False
            # print("\tLookUp Attr Table")
            # print(vars(y))
            return y
    return False


# def insertAttribute(name, params, ofType, accessMod, stat, concCond, ofName):
def insertMemberTable(name, params, Type, accessMod, stat, concCond, ofName):
    if(lookupMemberTable(name, params, ofName) == False):
        for i in mainTable_:
            if i.name == ofName:
                obj = MemberTable(name, params, Type,
                                     accessMod, stat, concCond)
                i.attrTable.append(obj)
                # print("\tAttr Table")
                # for t in i.attrTable:
                #     print(vars(t))
                return True
    return False


def lookupScopeTable(name):
    for i in scopeStack_:
        x = next((j for j in functionTable_ if j.scope ==
                 i and j.name == name), "")
        if (x != ""):
            # print("\tLookUp Func Table")
            # print(vars(x))
            return x.type
    # print("Undeclared -->", name)
    return False


def insertScopeTable(name, Type, scope):
    if(lookupScopeTable(name) == False):
        obj = ScopeTable(name, Type, scope)
        functionTable_.append(obj)
        # print("\tFunction Table")
        # for t in functionTable_:
        #     print(vars(t))
        return True
    # type = lookupScopeTable(name)
    print("REDECLARATION ---> "  , Type , name )
    return False

def InsertScopeTable(name, Type, scope):
    if(lookupScopeTable(name) == False):
        obj = ScopeTable(name, Type, scope)
        extraTable_.append(obj)
        # print("\tFunction Table")
        # for t in functionTable_:
        #     print(vars(t))
        return True
    # type = lookupScopeTable(name)
    # print("REDECLARATION ---> "  , Type , name )
    return False

def createScope():
    global highestScope
    highestScope += 1
    x = highestScope
    # print("createdScope:\t", x)
    scopeStack_.insert(0, x)
    return scopeStack_[0]


def destroyScope():
    x = scopeStack_.pop(0)
    # print("destroyedScope:\t", x)
    return scopeStack_[0]

# left = "int"
# right = "4"
# op = "="
def binTypeCompatible(left, right, op):
    check = left + right + op
    if check in typeCompatibility.keys():
        # print(typeCompatibility[check])
        return typeCompatibility[check]
        
    check = right + left + op
    if check in typeCompatibility.keys():
        # print(typeCompatibility[check])
        return typeCompatibility[check]
        
    # print("Type Mismatch Error")
    return False
# binTypeCompatible(left , right , op)


def uniTypeCompatible(left, op):
    check = left + op
    if check in typeCompatibility.keys():
        return typeCompatibility[check]
    return False