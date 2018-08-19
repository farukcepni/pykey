Generate random key by given rules.

Usage
====

>>> order_code_generator = PyKey(length=16, prefix='OI-',
                                 charset=PyKey.UPPERS + PyKey.DIGITS, repeated=False, adjacent=False)
>>> order_code_generator.get()
>>> OI-J5OHNVL0MIQ2S
>>> order_code_generator.get()
>>> OI-LTI8749HADOSR


>>> password_generator = PyKey(length=14, charset=PyKey.ALPHANUMERIC, repeated=True)
>>> password_generator.get()
>>> MwkazmsmDUKUZC
>>> password_generator.get()
>>> CDyNIjME6JLuZe
