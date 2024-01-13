import main  # import innego pliku do naszego pliku
import pakiet  # import całego pakietu (to co dopuscza __all__)
from pakiet import fun  # import konkretnego pliku z pakietu
import pakiet.fun as pk  # as pk oznacza import jako alias
from pakiet import fun2

main.print_hi("Test z innego pliku")

# from pakiet import fun
fun.powitanie()
fun.info()

# import pakiet.fun as pk
pk.powitanie()
pk.info()

# import pakiet
# __all__ = ['info']
pakiet.info()

# from pakiet import fun2
fun2.pozegnanie()

# __all__ = ['info','pozegnanie']
pakiet.pozegnanie()
