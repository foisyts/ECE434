#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void)
{
    uint32_t gpio = P9_31; //select which pin to toggle
    
    /* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
    CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;
    
    while(1){
        __R30 |= gpio;          // set GPIO pin to 1
        __delay_cycles(1000);
        __R30 |= ~gpio;         // set GPIO pin to 0
        __delay_cycles(1000);
    }
}