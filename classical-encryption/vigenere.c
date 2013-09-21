#include <stdio.h>
#include <stdlib.h>

int str_len(char* str);

char* encrypto(char* input, char* key);
char* decrypto(char* input, char* key);

int main(){
    char* key;
    char* proclaim;
    char* ciphertext;
    char* encrypto_result;
    char* decrypto_result;

    key = (char*)malloc(sizeof(char) * 100);
    proclaim = (char*)malloc(sizeof(char) * 100);
    ciphertext = (char*)malloc(sizeof(char) * 100);

    printf("Please input the proclaim:\n");
    scanf("%s", proclaim);
    printf("Please input the key for encrypto the text:\n");
    scanf("%s", key);
    encrypto_result = encrypto(proclaim, key);
    printf("Result: %s\n", encrypto_result);

    printf("Please input the text:\n");
    scanf("%s", ciphertext);
    printf("Please input the key for decrypto the text:\n");
    scanf("%s", key);
    decrypto_result = decrypto(ciphertext, key);
    printf("Result: %s\n", decrypto_result);

    free(key);
    free(proclaim);
    free(ciphertext);
    free(encrypto_result);
    free(decrypto_result);

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
    int rest = ptlen % key_len;

    char* output = (char*)malloc(sizeof(char) * 100);
    for (i=0;i<quotient;++i){
        for (j=0;j<key_len; ++j){
            int c = (input[i * key_len + j] - 97 + key[j] - 97) % 26 + 'a';
            output[index] = c;
            index ++;
        }
    }
    for (i=0;i<rest; ++i){
        int c = (input[quotient * key_len + i] - 97 + key[i] - 97) % 26 + 97;
        output[index] = c;
        index ++;
    }

    output[ptlen] = '\0';

    return output;
    
}

char* decrypto(char* input, char* key){
    int i, j;
    
    int index = 0;

    int key_len = str_len(key);
    int ptlen = str_len(input);

    int quotient = ptlen / key_len;
    int rest = ptlen % key_len;

    char* output = (char*)malloc(sizeof(char) * 100);
    for(i=0;i<quotient;++i){
        for(j=0;j<key_len;++j){
            int c = (input[i * key_len + j] - 97 + 26 - (key[j] - 97)) % 26 + 97;
            output[index] = c;
            index ++;
        }
    }
    for(i=0;i<rest; ++i){
        int c = (input[quotient * key_len + i] - 97 + 26 - (key[i] - 97)) % 26 + 97;
        output[index] = c;
        index ++;
    }
    
    output[ptlen] = '\0';

    return output;
}
