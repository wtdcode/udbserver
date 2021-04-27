from unicorn.x86_const import *
from unicorn.arm_const import *
from unicorn.arm64_const import *

reg_map_x86 = [
    [UC_X86_REG_EAX,     4],
    [UC_X86_REG_ECX,     4],
    [UC_X86_REG_EDX,     4],
    [UC_X86_REG_EBX,     4],
    [UC_X86_REG_ESP,     4],
    [UC_X86_REG_EBP,     4],
    [UC_X86_REG_ESI,     4],
    [UC_X86_REG_EDI,     4],
    [UC_X86_REG_EIP,     4],
    [UC_X86_REG_EFLAGS,  4],
    [UC_X86_REG_CS,      4],
    [UC_X86_REG_SS,      4],
    [UC_X86_REG_DS,      4],
    [UC_X86_REG_ES,      4],
    [UC_X86_REG_FS,      4],
    [UC_X86_REG_GS,      4],
]

reg_map_x64 = [
    [UC_X86_REG_RAX,     8],
    [UC_X86_REG_RBX,     8], 
    [UC_X86_REG_RCX,     8], 
    [UC_X86_REG_RDX,     8],
    [UC_X86_REG_RSI,     8], 
    [UC_X86_REG_RDI,     8],
    [UC_X86_REG_RBP,     8],
    [UC_X86_REG_RSP,     8], 
    [UC_X86_REG_R8,      8],
    [UC_X86_REG_R9,      8], 
    [UC_X86_REG_R10,     8],
    [UC_X86_REG_R11,     8],
    [UC_X86_REG_R12,     8], 
    [UC_X86_REG_R13,     8], 
    [UC_X86_REG_R14,     8],
    [UC_X86_REG_R15,     8],
    [UC_X86_REG_RIP,     8],
    [UC_X86_REG_EFLAGS,  4], 
    [UC_X86_REG_CS,      4], 
    [UC_X86_REG_SS,      4],
    [UC_X86_REG_DS,      4], 
    [UC_X86_REG_ES,      4], 
    [UC_X86_REG_FS,      4],
    [UC_X86_REG_GS,      4], 
]

reg_map_arm = [
    [UC_ARM_REG_R0,   4],
    [UC_ARM_REG_R1,   4],
    [UC_ARM_REG_R2,   4],
    [UC_ARM_REG_R3,   4],
    [UC_ARM_REG_R4,   4],
    [UC_ARM_REG_R5,   4],
    [UC_ARM_REG_R6,   4],
    [UC_ARM_REG_R7,   4],
    [UC_ARM_REG_R8,   4],
    [UC_ARM_REG_R9,   4],
    [UC_ARM_REG_R10,  4],
    [UC_ARM_REG_R11,  4],
    [UC_ARM_REG_R12,  4],
    [UC_ARM_REG_SP,   4],
    [UC_ARM_REG_LR,   4],
    [UC_ARM_REG_PC,   4],
]

reg_map_arm64 = [
    [UC_ARM64_REG_X0,   8],
    [UC_ARM64_REG_X1,   8],
    [UC_ARM64_REG_X2,   8],
    [UC_ARM64_REG_X3,   8],
    [UC_ARM64_REG_X4,   8],
    [UC_ARM64_REG_X5,   8],
    [UC_ARM64_REG_X6,   8],
    [UC_ARM64_REG_X7,   8],
    [UC_ARM64_REG_X8,   8],
    [UC_ARM64_REG_X9,   8],
    [UC_ARM64_REG_X10,  8],
    [UC_ARM64_REG_X11,  8],
    [UC_ARM64_REG_X12,  8],
    [UC_ARM64_REG_X13,  8],
    [UC_ARM64_REG_X14,  8],
    [UC_ARM64_REG_X15,  8],
    [UC_ARM64_REG_X16,  8],
    [UC_ARM64_REG_X17,  8],
    [UC_ARM64_REG_X18,  8],
    [UC_ARM64_REG_X19,  8],
    [UC_ARM64_REG_X20,  8],
    [UC_ARM64_REG_X21,  8],
    [UC_ARM64_REG_X22,  8],
    [UC_ARM64_REG_X23,  8],
    [UC_ARM64_REG_X24,  8],
    [UC_ARM64_REG_X25,  8],
    [UC_ARM64_REG_X26,  8],
    [UC_ARM64_REG_X27,  8],
    [UC_ARM64_REG_X28,  8],
    [UC_ARM64_REG_X29,  8],
    [UC_ARM64_REG_X30,  8],
    [UC_ARM64_REG_SP,   8],
    [UC_ARM64_REG_PC,   8],
]