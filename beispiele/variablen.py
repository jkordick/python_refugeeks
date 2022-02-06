# Variablen können mit verschiedenen Datentypen initialisiert werden
integer_var = 0  # int

float_var = 20.051  # float

string_var = "This is a String"  # str

boolean_var = True  # bool

null_var = None  # NoneType

# Überschreiben von Variablen
print(type(boolean_var))  # output: <class 'bool'>
boolean_var = "Boolean var is a string now"
print(type(boolean_var))  # output: <class 'str'>

# Casting von Variablen
# Explizit
float_to_string = str(float_var)
print(float_to_string, type(float_to_string))  # output: 20.051 <class 'str'>

# Implizit
int_var = 123  # int
float_var = 1.23  # float

new_var = int_var + float_var  # float
