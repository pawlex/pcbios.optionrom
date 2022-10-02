use16
dw 0xAA55   ; Option rom signature magic number
db 0x4      ; Option rom size (in 512 byte blocks)
align 8

; -----------------------------------

entry:
    push cs
    pop  ds
    ;
    jmp optionrom_entry
;

optionrom_entry:
    mov si, _message
    call print_string
    ; Halt the system when done
    .halt:
    hlt
    jmp .halt
;

print_string:
    .loop:
        lodsb
        cmp al, 0
        je .done
        call print_char
        jmp .loop
    .done:
        ret
;

print_char:
    ; AL should contain the char to print
    mov ah, 0x0E ; BIOS CALL
    mov bx, 0x0F ; BIOS CALL
    int 0x10
    ret
;

_message db 'Hello, world', 0

; Pad the remainder of the option rom
; 2K - 1, use csum8 to add the checksum byte.
times 2047-($-$$) db 90

