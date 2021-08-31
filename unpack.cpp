#include <cstdio>
#include<cstdlib>
#include <cerrno>
//#define FILE_PATH "/Users/howard1206/temp_raw_dump/01_w8192_h6144.RAWMIPI10"
//#define NEW_FILE_PATH "/Users/howard1206/temp_raw_dump/01_w8192_h6144.new_raw"
int rawConv(int width, int height, char *FILE_PATH, char *NEW_FILE_PATH);

int main(int argc, char *argv[]){
    //int width = 8192;
    //int height = 6144;
    rawConv(atoi(argv[1]), atoi(argv[2]), argv[3], argv[4]);
    return 0;
}
int rawConv(int width, int height, char *FILE_PATH, char *NEW_FILE_PATH){
    unsigned char ptr;
    unsigned short dst[4];
    unsigned char src[5];
    FILE *fsrc, *fdst;
    errno_t err;
    fsrc = fopen(FILE_PATH, "rb+");
    if (!fsrc) {
        printf( "read file failed %s\n", FILE_PATH);
        return 1;
    }
    
    fdst = fopen(NEW_FILE_PATH, "wb+");
    if(!fdst) {
        printf("create file failed %s!\n", NEW_FILE_PATH);
        return 1;
    }
    for (int i = 0; i < width*height; i+=4) {
        for (int j = 0; j <5; j++){
            fread(&ptr, 1, 1, fsrc);
            src[j] = ptr;
        }
        dst [0] = src[0];
        dst[0]<<= 2;
        dst [0] |= (src[4] & 0x3);
        
        dst[1] = src[1];
        dst[1] <<= 2;
        dst[1] |= (src[4] & 0x0c) >> 2;
        
        dst[2] = src[2];
        dst[2] <<= 2;
        dst[2] |= (src[4] & 0x30) >> 4;
        
        dst[3] = src[3];
        dst[3] <<= 2;
        dst[3] |= (src[4] & 0xc0) >> 6;
        
        fwrite(&dst[0], 1, sizeof(unsigned short), fdst);
        fwrite(&dst[1], 1, sizeof(unsigned short), fdst);
        fwrite(&dst[2], 1, sizeof(unsigned short), fdst);
        fwrite(&dst[3], 1, sizeof(unsigned short), fdst);
    }
    printf("convert success!!!\n");
    if (fsrc) {
        err = fclose(fsrc);
        if (err) {
            printf("close fsrc failedin");
            return 1;
        }
    }
    if(fdst){
        err = fclose(fdst);
        if (err) {
            printf("close fdst failed! \n");
            return 1;
        }
    }
    return 0;
}
