#session_2

print("Hello World")
print('2nd', end='')
print(' Cont. Line')

a= 20.20
t_a=type(a)
print(f"type of a={t_a}")
b= 30
c=a=b
t_c=type(c)
print(f"type of c={t_c}")
print("c=" + str(c))
print(f'c={c}')

i_a=3543543456364345345354354365435435436534653446354335465645546547
i_b=5475454765456475746456464564745465467456465465474754654654654766
max_int=i_a+i_b
print(f"max_int={max_int}")
s_a=str(i_a)
print(f'type(s_a)={type(s_a)}')
print(f'len(s_a)={len(s_a)}')

i_c=1.5e2
print(f'type(i_c)={type(i_c)}')
print(f'i_c={i_c}')

i_c=1.5e-2
print(f'type(i_c)={type(i_c)}')
print(f'i_c={i_c}')

i_c=1.545646545646546465465564654e100
print(f'type(i_c)={type(i_c)}')
print(f'i_c={i_c}')

i_c=1.545646545646546465465564654e10
print(f'type(i_c)={type(i_c)}')
print(f'i_c={i_c}')

h_a=0x1f
print(f'(h_a)={h_a}')
print(f'type(h_a)={type(h_a)}')
print(f'h_a={h_a}')

b_a=0b101010111
print(f'type(b_a)={type(b_a)}')
print(f'b_a={b_a}')