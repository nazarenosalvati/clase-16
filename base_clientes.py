from paquete.clientes import Cliente

cliente1 = Cliente("Joel", "Velazquez", 30, "joelv@gmail.com", "Responsable Inscripto")

print(cliente1.ver_cliente())

#Ahora actualizo el cliente

cliente1.actualizar_contacto("joelvelazquez@gmail.com")
print(cliente1.ver_cliente())