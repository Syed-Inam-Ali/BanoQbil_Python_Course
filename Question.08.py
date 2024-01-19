"""Question.08:
Create a complex number variable, comp_num, with real and 
imaginary parts.Print both parts separately.
 Understand the representation of complex numbers in Python."""
comp_num = 3 + 4j # Complex number declared
complex_no = complex(comp_num)
Re = complex_no.real
Im = complex_no.imag
print("Real part of your complex number is:",Re)
print("Imaginary part of your complex number is:",Im)