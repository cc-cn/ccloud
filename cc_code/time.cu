//这个代码的目的是比较cuda并行计算与普通cpu串行计算速度，在N=5000的时候，cuda需要1s，而cpu需要33s.随着N增大，这个差别将更加明显。
//当然这并不是一个好的并行计算代码。因为各个block之间的结果是互相影响的，这会导致并不能得到准确结果。

#include "../common/book.h"
#include<time.h>

#define N   5000


/*
int main()
{
	time_t begin,end; //time for seconds
    begin=time(NULL);
    int a;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<i;j++)
        {
            for(int k=0;k<j;k++)
            {
                a=j;
            }
        }
        
    }
    printf("%d\n",a);
    end=time(NULL);
	printf("use time %d s\n",int(end-begin));
	return 0;
}
*/
//*
__global__ void cc_copy( int *b, int *c ) {
    int tid = blockIdx.x;    // this thread handles the data at its thread id
    if (tid < N)
    {
        for(int j=0;j<b[tid];j++)
        {
            for(int k=0;k<j;k++)
            {
                *c=j;
            }
        }
    }
}


int main()
{
	time_t begin,end; //time for seconds
    begin=time(NULL);
    int b[N];
    for (int i=0; i<N; i++) {
        b[i] = i;
    }
    int *dev_b;
    HANDLE_ERROR( cudaMalloc( (void**)&dev_b, N * sizeof(int) ) );
    HANDLE_ERROR( cudaMemcpy( dev_b, b, N * sizeof(int),cudaMemcpyHostToDevice ) );
    int c;
    int* dev_c;
    HANDLE_ERROR( cudaMalloc( (void**)&dev_c, sizeof(int) ) );

    cc_copy<<<N,1>>>( dev_b,dev_c );

    // copy the array 'c' back from the GPU to the CPU
    HANDLE_ERROR( cudaMemcpy( &c, dev_c, sizeof(int),cudaMemcpyDeviceToHost ) );

    printf("%d\n",c);
    end=time(NULL);
	printf("use time %d s\n",int(end-begin));
	return 0;
}
//*/