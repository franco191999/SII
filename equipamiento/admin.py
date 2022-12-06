from django.contrib import admin
from equipamiento.models import *

class admin_nom_tipo_pc(admin.ModelAdmin):
	pass
admin.site.register(nom_tipo_pc, admin_nom_tipo_pc)


class admin_so(admin.ModelAdmin):
	pass
admin.site.register(so, admin_so)


class admin_estado(admin.ModelAdmin):
	pass
admin.site.register(estado, admin_estado)


class admin_pc(admin.ModelAdmin):
	pass
admin.site.register(pc, admin_pc)


class admin_nom_board_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_board_marca, admin_nom_board_marca)


class admin_nom_socket(admin.ModelAdmin):
	pass
admin.site.register(nom_socket, admin_nom_socket)


class admin_board_pc(admin.ModelAdmin):
	pass
admin.site.register(board_pc, admin_board_pc)


class admin_nom_procesador_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_procesador_marca, admin_nom_procesador_marca)


class admin_nom_procesador_velocidad(admin.ModelAdmin):
	pass
admin.site.register(nom_procesador_velocidad, admin_nom_procesador_velocidad)


class admin_procesador(admin.ModelAdmin):
	pass
admin.site.register(procesador, admin_procesador)


class admin_nom_ram_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_ram_marca, admin_nom_ram_marca)


class admin_nom_ram_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_ram_tipo, admin_nom_ram_tipo)


class admin_nom_ram_velocidad(admin.ModelAdmin):
	pass
admin.site.register(nom_ram_velocidad, admin_nom_ram_velocidad)


class admin_ram(admin.ModelAdmin):
	pass
admin.site.register(ram, admin_ram)


class admin_nom_hdd_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_hdd_marca, admin_nom_hdd_marca)


class admin_nom_hdd_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_hdd_tipo, admin_nom_hdd_tipo)


class admin_nom_hdd_capacidad(admin.ModelAdmin):
	pass
admin.site.register(nom_hdd_capacidad, admin_nom_hdd_capacidad)


class admin_hdd(admin.ModelAdmin):
	pass
admin.site.register(hdd, admin_hdd)


class admin_nom_cddvd_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_cddvd_marca, admin_nom_cddvd_marca)


class admin_nom_cddvd_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_cddvd_tipo, admin_nom_cddvd_tipo)


class admin_nom_cddvd_utilidad(admin.ModelAdmin):
	pass
admin.site.register(nom_cddvd_utilidad, admin_nom_cddvd_utilidad)


class admin_cddvd(admin.ModelAdmin):
	pass
admin.site.register(cddvd, admin_cddvd)


class admin_nom_fuente_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_fuente_marca, admin_nom_fuente_marca)


class admin_nom_fuente_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_fuente_tipo, admin_nom_fuente_tipo)


class admin_fuente(admin.ModelAdmin):
	pass
admin.site.register(fuente, admin_fuente)


class admin_nom_tvideo_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_tvideo_marca, admin_nom_tvideo_marca)


class admin_nom_tvideo_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_tvideo_tipo, admin_nom_tvideo_tipo)


class admin_tvideo(admin.ModelAdmin):
	pass
admin.site.register(tvideo, admin_tvideo)


class admin_nom_tsonido_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_tsonido_marca, admin_nom_tsonido_marca)


class admin_nom_tsonido_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_tsonido_tipo, admin_nom_tsonido_tipo)


class admin_tsonido(admin.ModelAdmin):
	pass
admin.site.register(tsonido, admin_tsonido)


class admin_nom_tred_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_tred_marca, admin_nom_tred_marca)


class admin_nom_tred_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_tred_tipo, admin_nom_tred_tipo)


class admin_nom_tred_velocidad(admin.ModelAdmin):
	pass
admin.site.register(nom_tred_velocidad, admin_nom_tred_velocidad)


class admin_tred(admin.ModelAdmin):
	pass
admin.site.register(tred, admin_tred)


class admin_nom_chasis_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_chasis_marca, admin_nom_chasis_marca)


class admin_nom_chasis_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_chasis_tipo, admin_nom_chasis_tipo)


class admin_chasis(admin.ModelAdmin):
	pass
admin.site.register(chasis, admin_chasis)


class admin_nom_modem_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_modem_marca, admin_nom_modem_marca)


class admin_nom_modem_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_modem_tipo, admin_nom_modem_tipo)


class admin_modem(admin.ModelAdmin):
	pass
admin.site.register(modem, admin_modem)


class admin_nom_teclado_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_teclado_marca, admin_nom_teclado_marca)


class admin_nom_teclado_raton_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_teclado_raton_tipo, admin_nom_teclado_raton_tipo)


class admin_teclado(admin.ModelAdmin):
	pass
admin.site.register(teclado, admin_teclado)


class admin_nom_raton_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_raton_marca, admin_nom_raton_marca)


class admin_raton(admin.ModelAdmin):
	pass
admin.site.register(raton, admin_raton)


class admin_nom_bocinas_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_bocinas_marca, admin_nom_bocinas_marca)


class admin_nom_monitor_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_monitor_marca, admin_nom_monitor_marca)


class admin_nom_monitor_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_monitor_tipo, admin_nom_monitor_tipo)


class admin_nom_monitor_dimension(admin.ModelAdmin):
	pass
admin.site.register(nom_monitor_dimension, admin_nom_monitor_dimension)


class admin_monitor(admin.ModelAdmin):
	pass
admin.site.register(monitor, admin_monitor)


class admin_nom_impresora_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_impresora_marca, admin_nom_impresora_marca)


class admin_nom_impresora_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_impresora_tipo, admin_nom_impresora_tipo)


class admin_nom_impresora_interface(admin.ModelAdmin):
	pass
admin.site.register(nom_impresora_interface, admin_nom_impresora_interface)


class admin_impresora(admin.ModelAdmin):
	pass
admin.site.register(impresora, admin_impresora)


class admin_nom_scanner_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_scanner_marca, admin_nom_scanner_marca)


class admin_nom_scanner_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_scanner_tipo, admin_nom_scanner_tipo)


class admin_nom_scanner_dimension(admin.ModelAdmin):
	pass
admin.site.register(nom_scanner_dimension, admin_nom_scanner_dimension)


class admin_nom_scanner_interface(admin.ModelAdmin):
	pass
admin.site.register(nom_scanner_interface, admin_nom_scanner_interface)


class admin_scanner(admin.ModelAdmin):
	pass
admin.site.register(scanner, admin_scanner)


class admin_nom_ups_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_ups_marca, admin_nom_ups_marca)


class admin_nom_ups_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_ups_tipo, admin_nom_ups_tipo)


class admin_ups(admin.ModelAdmin):
	pass
admin.site.register(ups, admin_ups)


class admin_nom_switch_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_switch_marca, admin_nom_switch_marca)


class admin_nom_switch_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_switch_tipo, admin_nom_switch_tipo)


class admin_switch(admin.ModelAdmin):
	pass
admin.site.register(switch, admin_switch)


class admin_nom_camara_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_camara_marca, admin_nom_camara_marca)


class admin_nom_camara_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_camara_tipo, admin_nom_camara_tipo)


class admin_camara(admin.ModelAdmin):
	pass
admin.site.register(camara, admin_camara)


class admin_nom_stick_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_stick_marca, admin_nom_stick_marca)


class admin_nom_stick_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_stick_tipo, admin_nom_stick_tipo)


class admin_stick(admin.ModelAdmin):
	pass
admin.site.register(stick, admin_stick)


class admin_nom_ap_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_ap_marca, admin_nom_ap_marca)


class admin_nom_ap_tipo(admin.ModelAdmin):
	pass
admin.site.register(nom_ap_tipo, admin_nom_ap_tipo)


class admin_ap(admin.ModelAdmin):
	pass
admin.site.register(ap, admin_ap)



