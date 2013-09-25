#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define STATE_LENGTH 256
#define MAX_LENGTH 256
typedef unsigned char byte;

byte* state;

char* ByteToHex(byte* text);
byte* HexToByte(const char* text);
void swapByte(byte* lp, byte* rp);
int getLen(const char* str);
int getLen(byte* str);
void KSA(const char* keyBytes);
byte* transfroms(const char* input);
byte* processBytes(byte* text, int length);
char* encrypto(const char* text, const char* key);
byte* decrypto(const char* text, const char* key);

int main(){
    char* input = (char*) malloc(sizeof(char) * MAX_LENGTH);
    char* key = (char*) malloc(sizeof(char) * MAX_LENGTH);

    printf("Please input the text.\n");
    scanf("%s", input);
    printf("Please input the key.\n");
    scanf("%s", key);

    printf("Encrypto: %s\n", encrypto(input, key));
    printf("Decrypto: %s", decrypto(encrypto(input, key), key));
    
    return 0;
}

char* ByteToHex(byte* text){
    if (text == NULL){
        return NULL;
    }
    int i, high, low;
    int length = getLen(text);
    char* hex = (char*) malloc(sizeof(char) * (length * 2 + 1));

    for (i=0; i<length; ++i){
        high = (int)(text[i]) / 16;
        low = (int)(text[i]) % 16;
        hex[i * 2] = (char) (high + ((high > 9) ? 'A' - 10 : '0'));
        hex[i * 2 + 1] = (char) (low + ((low > 9) ? 'A' - 10 : '0'));
    }

    hex[2 * length] = '\0';
    return hex;
}

byte* HexToByte(const char* text){
    if (text == NULL){
        return NULL;
    }

    int i;
    int high, low;
    int length = getLen(text);
    byte* bytes = (byte*)malloc(sizeof(byte) * ((int)(length/2) + 1));
    for (i=0; i<length/2; ++i){
        high = (int)text[i*2] - (((int)text[i*2] >= 'A') ? 'A' - 10 : '0');
        low = (int)text[i*2+1] - (((int)text[i*2+1] >= 'A') ? 'A' - 10 : '0');
        if (high >= 16 || low >= 16){
            return NULL;
        }
        bytes[i] = (high * 16 + low);
    }
    bytes[(int)(length/2)] = '\0';
    return bytes;
}

void swapByte(byte* lp, byte*rp){
    byte temp = *lp;
    *lp = *rp;
    *rp = temp;
}

int getLen(const char* str){
    int i = 0;
    while(str[i] != '\0'){
        i++;
    }
    return i;
}

int getLen(byte* str){
    int i = 0;
    while(str[i] != '\0'){
        i++;
    }
    return i;
}

void KSA(const char* keyBytes){
    int i, j=0;
    int key_len = getLen(keyBytes);
    byte* workingKey = (byte*) malloc(sizeof(byte) * STATE_LENGTH);
    state = (byte*) malloc(sizeof(byte) * STATE_LENGTH);

    for (i=0;i<STATE_LENGTH;++i){
        state[i] = i;
    }
    for (i=0;i<STATE_LENGTH;++i){
        j = (j + state[i] + keyBytes[i % key_len]) % STATE_LENGTH;
        swapByte(&state[i], &state[j]);
    }
}

byte* processBytes(byte* text){
    int i, x=0, y=0;
    int length = getLen(text);
    byte* output = (byte*)malloc(sizeof(byte) * length);
    for (i=0;i<length;++i){
        x = (x + 1) % STATE_LENGTH;
        y = (state[x] + y) % STATE_LENGTH;
        swapByte(&state[x], &state[y]);
        output[i] = text[i] ^ state[(state[x] + state[y]) % STATE_LENGTH];
    }
    output[length] = '\0';
    return output;
}

char* encrypto(const char* rawText, const char* key){
    int i;
    byte* text = (byte*) malloc(sizeof(byte) * getLen(rawText));
    memcpy(text, rawText, getLen(rawText) + 1);
    KSA(key);
    byte* output = processBytes(text);
    return ByteToHex(output);
}

byte* decrypto(const char* text, const char* key){
    KSA(key);
    byte* bytes = HexToByte(text);
    byte* output = (byte*)processBytes(bytes);
    return output;
}
