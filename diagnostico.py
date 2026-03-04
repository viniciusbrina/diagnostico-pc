#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Diagnóstico de PC
Autor: Vinicius Feliciano Brina
Descrição: Script para diagnóstico automático de hardware e software
"""

import platform
import psutil
import os
from datetime import datetime

def obter_info_sistema():
    """Coleta informações do sistema"""
    print("="*50)
    print("DIAGNÓSTICO DO SISTEMA")
    print("="*50)
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("\n--- SISTEMA OPERACIONAL ---")
    print(f"Sistema: {platform.system()}")
    print(f"Versão: {platform.version()}")
    print(f"Arquitetura: {platform.machine()}")
    print(f"Processador: {platform.processor()}")

def obter_info_hardware():
    """Coleta informações de hardware"""
    print("\n--- HARDWARE ---")
    # CPU
    print(f"Núcleos CPU: {psutil.cpu_count(logical=False)}")
    print(f"Threads: {psutil.cpu_count(logical=True)}")
    print(f"Uso CPU: {psutil.cpu_percent(interval=1)}%")
    
    # Memória
    mem = psutil.virtual_memory()
    print(f"\nMemória Total: {mem.total / (1024**3):.2f} GB")
    print(f"Memória Disponível: {mem.available / (1024**3):.2f} GB")
    print(f"Memória em Uso: {mem.percent}%")
    
    # Disco
    print("\n--- DISCOS ---")
    for particao in psutil.disk_partitions():
        try:
            uso = psutil.disk_usage(particao.mountpoint)
            print(f"\nDisco: {particao.device}")
            print(f"  Tipo: {particao.fstype}")
            print(f"  Total: {uso.total / (1024**3):.2f} GB")
            print(f"  Usado: {uso.used / (1024**3):.2f} GB ({uso.percent}%)")
            print(f"  Livre: {uso.free / (1024**3):.2f} GB")
        except:
            pass

def verificar_saude():
    """Verifica a saúde do sistema"""
    print("\n--- VERIFICAÇÃO DE SAÚDE ---")
    
    # Verifica uso de CPU
    cpu_uso = psutil.cpu_percent(interval=1)
    if cpu_uso > 80:
        print("⚠️  ALERTA: Uso de CPU elevado ({cpu_uso}%)")
    else:
        print("✅ CPU: Normal")
    
    # Verifica uso de memória
    mem_uso = psutil.virtual_memory().percent
    if mem_uso > 85:
        print(f"⚠️  ALERTA: Uso de memória elevado ({mem_uso}%)")
    else:
        print("✅ Memória: Normal")
    
    # Verifica espaço em disco
    for particao in psutil.disk_partitions():
        try:
            uso = psutil.disk_usage(particao.mountpoint)
            if uso.percent > 90:
                print(f"⚠️  ALERTA: Disco {particao.device} quase cheio ({uso.percent}%)")
        except:
            pass

def main():
    """Função principal"""
    try:
        obter_info_sistema()
        obter_info_hardware()
        verificar_saude()
        
        print("\n" + "="*50)
        print("Diagnóstico concluído!")
        print("="*50)
        
    except Exception as e:
        print(f"\nErro ao executar diagnóstico: {e}")

if __name__ == "__main__":
    main()
    input("\nPressione ENTER para sair...")
