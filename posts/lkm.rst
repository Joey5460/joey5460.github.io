LKM(loadable kernel module) programming
---------------------------------------
Reference: 
   - https://gist.github.com/anryko/c8c8788ccf7d553a140a03aba22cab88

Install
   - sudo dnf install kernel-devel

Kernel module example 
    .. code:: c

      #include <linux/module.h>       // Needed by all modules
      #include <linux/kernel.h>       // KERN_INFO

      int init_module(void)
      {
           printk(KERN_INFO "== Loading s2fs module ==\n");

           return 0;
      }

      void cleanup_module(void)
      {
           printk(KERN_INFO "== Exit s2fs module ==\n");
      }

      MODULE_LICENSE("MIT");


Makefile
   .. code-block:: makefile

      obj-m += lkm_test.o
      KDIR ?= /lib/modules/$(shell uname -r)/build

      all:
              make -C $(KDIR) M=$(PWD) modules

      clean:
              make -C $(KDIR) M=$(PWD) clean

      load:
              sudo insmod lkm_test.ko

      unload:
              sudo rmmod lkm_test
Test
   ::

      dmesg -w
      make load

command
   - insmod
   - rmmod
   - lsmod
