
#Demo_0

def demo_0():
    """(Un)packing Dict key-values."""
    
    kw2='kw2'
    dict ={'kw1':"goo", kw2:2, 5.5:'55'}
    #*** kw may be of any hashable type,
    #*** not only string, not list
    
    print(dict) 
    # print unpacked dict
    #>>>:{'kw1': 'goo', 'kw2': 2, 5.5: 
    #>>>'55'}
    
    a,b,c = dict # unpacking without *
    print(a,b,c) # prints all kws   
    a,b,c = dict['kw1'] 
    print(a,b,c)#prints all kw1 subvalues
    
    print(*dict) 
    # half-unpacked
    #>>>: d1 d2. 
    #--->No error since non 
    # kw args, but positional ones
    
    #print(**dict)# fully unpacked dict
    #---> print accepts its own kw args
    #>>>TypeError: 'd1' is an invalid 
    #>>>keyword argument for this function
    
    
def demo_0_1():
    """ Packing/unpacking values."""
    
    list =[1,2]
    
    list.append(3)#[OK]>>>None
    #a,b,c =  list.append(3) #[FAIL] 
    #---> can't assign 'None' to a,b,c
    
    #a,b=(*list)#[Fail] !!! 
    # explicit unpacking didn't work
    
    print("list unpacking to vars")
    a,b,c =  list#[OK] 
    print(a,b,c)#>>>1 2 3
    
    print("range unpacking to vars")
    a,b,c = range(1,4)
    print(a,b,c)
    print("range unpacked with '*'")
    print(*range(1,4))
    print("range without unpacking")
    print(range(1,4))
    
    print("list without unpacking")
    print(list)
    #>>>[1, 2, 3]
    # printed packed values as one val
    
    print("list unpacked with '*'")
    print(*list)#>>>1 2 
    # unpacked values passed.
    # multiple pos args allowed 
    # in print function definition
    
def demo_0_2():
    """ Std args usg on func call stage.
    
        Rule: no pos args after kw args.
    """
    
    def f(a,b,c):
        print(a,b,c)
    f(1,c=2,b=3)#[OK]
    #f(a=5, 6, 7)#[FAIL] 
    # ? no explicit identification
    #f(c=6, a=7, 8)#[FAIL] 
    #--> even it could have inferred 'b'
    f(9,8,7)#[OK]

# Demo_1
def demo_1():
    """Unlim kw args in function def."""
        
    def f(**args):
        #**args is a formal parameter
        #fun accepts arbitrary number of 
        #kw=val arguments
        #(kw1=val1,kw2=val2,...)
        for arg in args:
            print('key:',arg,'\tvalue:',
                args[arg])
    
    dict ={'d1':["goo","woo"], 'd2':2}
    #!!!dict can accept list as a value
    #!!!but not as a key
    
    # check points:
        
    #f(dict)#[Fail] Only kw args allowed
    #--->TypeError: f() takes 0
    #--->positional arguments but 1 was 
    #--->given
    
    #f(*dict)#[Fail] kw without val given
    #--->TypeError: f() takes 0 positional 
    #--->arguments but 2 were given
    
    print("feed non-packed kw args")
    f(a=1, b=2, c=3)#[OK] 
    
    print("feed packed 'kw=val' args")
    f(**dict)#[OK] 
    #dict=dict + ({'e5':55})#[F]
    
    print("feed non-packed&packed kw args")
    f(k1="ddd", k2="sss",k3='ggg',
      **dict)#[OK] 

def demo_3(a: int):
    """ Annotation example."""
    
    return a+'10'
        
def demo4():
    """ Three types of arguments.
    # this interpreter doesn't 
    # support (a,/,b,*,c=1) syntax


    Positional only: before '/'
    Standard (mixed) arguments: after '/'
    Keyword only arguments: after '*' """
    
    def pos_only(arg1,arg2,arg3,/):
        """Positional-only, non-default"""
        print(pos_only.__doc__)
        print(arg1,arg2,arg3)
        
    pos_only(555,666,777)
    
    
def demo5(**kw):
    """Passing ways for kw-only params."""
    
    def pass1(**kw):
        """Multiple params through **kw"""
        print(pass1.__doc__)    
        if (type(kw)==type({})):
            for arg, val in kw.items():
                print("param",arg,val)
    def pass2(kw=None):
        """Multiple params through Dict"""
        print(pass2.__doc__)    
        if (type(kw)==type({})):
            for arg, val in kw.items():
                print("param",arg,val)
                
    print("1.", demo5.__doc__)
    
    print()
    print("1.1.Non-packed param passings")
    #
    print()
    print("a)Passing variable param keys")
    k1,k2,kN = 44411,55511,100011
    print("Vars' GUIs:",'k1','k2','kN')
    print("Vars' Vals:", k1, k2, kN)
    pass1(k1='v1', k2='v2', kN='vN')#[OK]
    pass2({k1:'v1', k2:'v2',kN:'vN'})#[OK]
   
    print()
    print("b)Passing variable param vals")
    v1,v2,vN = 44411,55511,100011
    pass1(k1=v1, k2=v2, kN=vN)#[OK]
    pass2({'k1':v1, 'k2':v2,'kN':vN})#[OK]
    
    print()
    print('c)Passing params as vars')
    pass1(k1=444, k2=555, kN=1000)
    pass2({'k1':444, 'k2':555,'kN':1000})
    # [OK] for both
    
    print()
    print("1.2.Packed param passings")
    
    print("\n Passing non-str param keys")
    dict={1:'pos',2:'strd',3:'kw'}
    #pass1(**dict)#[F]Keys should be str
    pass2(dict)#[OK] No str restriction
    
    print("0 param pass")
    pass1()#[OK] 0 or more params
    pass2()#[OK] default value

g_var0 ="I'm global/top level variable"
def demo6():
    """Accessing higher level vars."""
    
    print(demo6.__doc__)
    g_var1 ="I'm first level variable"
    def inner_fun():
        print("top level gvar:",g_var0)
        #[OK] accessed global var
        #g_var0="gggg"#[F] overrides g_var
        
        print("1st level gvar:",g_var1)
        #[OK] accessed global var
        #g_var="gggg"#[F] overrides g_var
    inner_fun()
    print("top level gvar:",g_var0)#)
    
####
#$$$$
####
#demo_0()
#demo_0_1()
demo4()
