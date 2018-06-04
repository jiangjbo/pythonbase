#!/bin/bash
cpu_idle=`top -n2 | grep 'Cpu' | tail -n 1 | awk '{print $8}'`
cpu_usage=`echo "100 - $cpu_idle" | bc`

mem_free=`free -m | awk '/Mem:/{ print $4 + $6 + $7'}`
mem_total=`free -m | awk '/Mem:/{ print $2'}`
mem_used=`echo "$mem_total - $mem_free" | bc`
mem_rate=`echo "$mem_used * 100 / $mem_total" | bc`




