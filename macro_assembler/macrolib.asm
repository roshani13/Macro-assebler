%macro str_len 1
	mov edi,%1
	mov esi,edi
	mov al,0
	cld
	repne scasb
	sub edi,esi
	dec edi
	mov eax,edi
%endmacro

%macro str_copy 1
	mov esi,%1
	mov edi,src
	push ecx
	push edi
	str_len esi
	pop edi
	mov ecx,eax
	cld
	repne movsb
	pop ecx
%endmacro
	
section .data
	str1 db "madam",0
	len equ $-str1
	str2 db "gram",0
	len2 equ $-str2
	msg db "%d",10,0

section .bss
	src resb 20
	cnt resd 1
