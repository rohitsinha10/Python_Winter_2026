s1='abcdef'
print(f's1={s1}')
s1_sub=s1[0:4]
print(f's1_sub={s1_sub}')
s2_sub=s1[:4]
print(f's1_sub={s1_sub}')
s3_sub=s1[4]
print(f's1_sub={s1_sub}')

#single line comment

'''multi
line
comment'''

a=9
b='9'
print(f'type(a)={type(a)}, type(b)={type(b)}')
print(f'a={a}, b={b}')

s_a=str(a)
s_a='2.3243'
i_a=int(s_a)
print(f'type(i_a)={type(i_a)}, type(s)={type(s)}')
print(f'i_a={i_a}, b={b}')

s_b=3322323 #will work with int (2323.3234) or even with e (232.223e10), but not anything else (23.223df6) will give error
f_a=float(s_b)
print(f'type(f_a)={type(f_a)}')
print(f'f_a={f_a}')

s1='affdfd'
s2='ddfsgs'
print(f's1={s1}, s2={s2}')
s3=s1+s2
print(f's3={s3}')
len_s3=len(s3)
print(f'len_s3={len_s3}')

sub_ind=s3.find('af')
print(f'sub_ind={sub_ind}')

sub_ind=s3.rfind('af')
print(f'sub_ind={sub_ind}')

#find will search from left, rfind will do from right