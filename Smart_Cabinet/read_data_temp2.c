#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <math.h>
#include "mraa.h"
int container=1,sensor_id,sensor_stat[1];
uint16_t weights[4];
int i,powers[4],sum,total_weight;
FILE *fp;

int main ()
{
	mraa_aio_context aio0,aio1,aio2,aio3;
	aio0=mraa_aio_init(0);
	aio1=mraa_aio_init(1);
	aio2=mraa_aio_init(2);
	aio3=mraa_aio_init(3);

//	while(1)
//	{
	
	
	   fp =fopen("/media/sdcard/smart_cabinet.txt","w");
		weights[0]=mraa_aio_read(aio0);
		weights[1]=mraa_aio_read(aio1);
		weights[2]=mraa_aio_read(aio2);
		weights[3]=mraa_aio_read(aio3);
		//printf("%d",adc_value[0]);
		printf("\n CHECK \t");
		sum=0;
		for(i=0;i<4;i++)
		{
			powers[i]=0;
			if(weights[i]>200 && weights[i]<2000)
				powers[i]=pow(2,i);
			sum=sum+powers[i];
		}
		//adc_value[1]=mraa_aio_read(aio1);
		//printf("%d",adc_value[1]);
		//adc_value[2]=mraa_aio_read(aio2);
		//printf("%d",adc_value[2]);
		//adc_value[3]=mraa_aio_read(aio3);
		//printf("%d",adc_value[3]);
/*for(i=0;i<3;i++)
		{
			if(adc_value[i] < threshold && sensor_stat[i] ==0)
			{

			   sensor_stat[i]=1;
			}
			else if(adc_value[i] > threshold && sensor_stat[i] ==1)
			{
			   sensor_stat[i]=0;

			}
		}*/
	total_weight=sum*120;
		printf("%d %d  %d %d \n",weights[0],weights[1],weights[2],weights[3]);
	printf("total weight is %d \n",total_weight);
		fprintf(fp,"%s$%d","container1",total_weight);
		//fprintf(fp,"%d$%d$%d$%d\n",mother_id,1,sensor_stat[1],adc_value[1]);
		//fprintf(fp,"%d$%d$%d$%d\n",mother_id,2,sensor_stat[2],adc_value[2]);
		//fprintf(fp,"%d$%d$%d$%d\n",mother_id,3,sensor_stat[3],adc_value[3]);
		printf("finished writing to file\n");

		 fclose(fp);
		
//	}

  return 0;
}




