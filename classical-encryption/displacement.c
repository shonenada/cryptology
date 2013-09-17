#include <stdio.h>
#include <stdlib.h>

char encrypto_char(char c, int key);
void encrypto(char* input, int key);

char decrypto_char(char c, int key);
void decrypto(char* input, int key);

int main(){
    int key;
    char* proclaim;
    char* ciphertext;
    proclaim = (char*)malloc(sizeof(char) * 100);
    ciphertext = (char*)malloc(sizeof(char) * 100);
    printf("Please input the key for encrypto the text:\n");
    scanf("%d", &key);
    printf("Please input the proclaim:\n");
    scanf("%s", proclaim);
    encrypto(proclaim, key);
    printf("Encrypto result: %s\n", proclaim);
    printf("Please input the key for decrypto the text:\n");
    scanf("%d", &key);
    printf("Please input the cipher text:\n");
    scanf("%s", ciphertext);
    decrypto(ciphertext, key);
    printf("Decrypto result: %s\n", ciphertext);
    free(proclaim);
    free(ciphertext);
    return 0;
}

char encrypto_char(char c, int key){
    char output;

    output = (c - 97 + key) % 26 + 97;
    
    return output;
}

void encrypto(char* input, int key){
    int i=0;
    while(input[i] != '\0'){
        input[i] = encrypto_char(input[i], key);
        i = i + 1;
    }
}

char decrypto_char(char c, int key){
    char output;
    output = c - 97 - key;
    if (output >= 0){
        return (output % 26 + 97);
    }else{
        return (output + 97 + 26);
    }
}

void decrypto(char * input, int key){
    int i=0;
    while(input[i] != '\0'){
        input[i] = decrypto_char(input[i], key);
        i = i + 1;
    }
}
