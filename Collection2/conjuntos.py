#trabalhando com conjuntos
estuda_python={15,42,25,67}
estuda_javascript={42,4,48,67}

estudam_1_ao_menos= estuda_javascript|estuda_python
estudam_os_2= estuda_python & estuda_javascript
estudam_somente_1=estuda_javascript ^ estuda_python

print("""{} estudam ao menos uma linguagem.\n 
{} estudam as 2 linguagens. \n {} estudam somente 1 linguagem"""
.format(len(estudam_1_ao_menos),len(estudam_os_2),len(estudam_somente_1)))

