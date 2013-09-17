#include <stdio.h>
#include <stdlib.h>

int str_len(char* str);

char* encrypto(char* input, char* key);
char* decrypto(char* input, char* key);

int main(){
    char* key;
    char* proclaim;
    char* ciphertext;

    key = (char*)malloc(sizeof(char) * 100);
    proclaim = (char*)malloc(sizeof(char) * 100);
    ciphertext = (char*)malloc(sizeof(char) * 100);

    printf("Please input the key for encrypto the text:\n");
    scanf("%s", key);
    printf("Please input the proclaim:\n");
    scanf("%s", proclaim);
    proclaim = encrypto(proclaim, key);
    printf("Result: %s\n", proclaim);

    printf("Please input the key for decrypto the text:\n");
    scanf("%s", key);
    printf("Please input the text:\n");
    scanf("%s", ciphertext);
    ciphertext = decrypto(ciphertext, key);
    printf("Result: %s\n", ciphertext);

    free(key);
    free(proclaim);
    free(ciphertext);

    return 0;
}

int str_len(char* str){
    int i=0;
    while(str[i] != '\0'){
        i++;
    }
    return i;
}

char* encrypto(char* input, char *key){
    int i, j;
    int index = 0;

    int key_len = str_len(key);
    int ptlen = str_len(input);

    int quotient = ptlen / key_len;
    int remainder = ptlen % key_len;

    char* output = (char*)malloc(sizeof(char) * 100);
    for (i=0;i<quotient;++i){
        for (j=0;j<key_len; ++j){
            int c = (input[i * key_len + j] - 97 + key[j] - 97) % 26 +'a';
            output[index] = c;
            index ++;
        }
    }
    for (i=0;i<remainder; ++i){
        int c = (input[quotient * key_len + i] - 97 + key[i] - 97) % 26 + 97;
        output[index] = c;
        index ++;
    }

    return output;
    
}

char* decrypto(char* input, char* key){
    int i, j;
    
    int index = 0;

    int key_len = str_len(key);
    int ptlen = str_len(input);

    int quotient = ptlen / key_len;
    int remainder = ptlen % key_len;

    char* output = (char*)malloc(sizeof(char) * 100);
    for(i=0;i<quotient;++i){
        for(j=0;j<key_len;++j){
            int c = (input[i * key_len + j] - 97 + 26 - (key[j] - 97)) % 26 + 97;
            output[index] = c;
            index ++;
        }
    }
    for(i=0;i<remainder; ++i){
        int c = (input[quotient * key_len + i] - 97 + 26 - (key[i] - 97)) % 26 + 97;
        output[index] = c;
        index ++;
    }
    return output;
}
