cmd_output/bin/cluster_bin := /usr/local/k1tools/bin/k1-g++ -o output/bin/cluster_bin    output/build/cluster_bin_build/slave.cpp.o output/build/cluster_bin_build/__/__/include/mppa_utils.cpp.o   -mcluster=node -L/home/lig-ext/marquesb/project/pskel/apps/gol/output/lib/cluster/   -g -mhypervisor -lm -Wl,--defsym=USER_STACK_SIZE=0x2000 -Wl,--defsym=KSTACK_SIZE=0x1000 -lgomp -pthread -lmppa_remote -lmppa_async -lmppa_request_engine -lmppapower -lmppanoc -lmpparouting -Wl,--defsym=_LIBNOC_DISABLE_FIFO_FULL_CHECK=0 -march=k1b -mboard=developer -mos=nodeos   
