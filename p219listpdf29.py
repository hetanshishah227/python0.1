procedural = ["c", "fortran", "pascal"]
object_oriented = ["java", "c++", "python"]
functional = ["haskell", "scala", "lisp"]

lang = input("Enter programming language=>").lower()
if lang in procedural:
    print("Paradigm is procedural")
elif lang in object_oriented:
    print("Paradigm is Object Oriented")
elif lang in functional:
    print("Paradigm is functional")
else:
    print("Enter one of these languages=>c,fortran,pascal,java,c++,python,haskell,lisp,scala")