#include <stdio.h>
#include <stdlib.h>

void encrypto(char* input, int key);
void decrypto(char* input, int key);

int main(){
    int key;
    char* proclaim;
    char* ciphertext;

    proclaim = (char*)malloc(sizeof(char) * 100);
    ciphertext = (char*)malloc(sizeof(char) * 100);

    printf("Please input the proclaim:\n");
    scanf("%s", proclaim);
    printf("Please input the key for encrypto the text:\n");
    scanf("%d", &key);
    encrypto(proclaim, key);
    printf("Encrypto result: %s\n", proclaim);

    printf("Please input the cipher text:\n");
    scanf("%s", ciphertext);
    printf("Please input the key for decrypto the text:\n");
    scanf("%d", &key);
    decrypto(ciphertext, key);
    printf("Decrypto result: %s\n", ciphertext);

    getchar();getchar();

    free(proclaim);
    free(ciphertext);

    return 0;
}

void encrypto(char* input, int key){
    int i=0;
    while(input[i] != '\0'){
        input[i] = (input[i] - 97 + key) % 26 + 97;
        i = i + 1;
    }
}

void decrypto(char * input, int key){
    int i=0;
    key = key % 26;
    while(input[i] != '\0'){
        int temp = input[i] - 97 - key;
        if (temp >= 0){
            input[i] = temp % 26 + 97;
        }else{
            input[i] = input[i] + 26 - key;
        }
        i = i + 1;
    }
}
