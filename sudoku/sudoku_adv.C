#include<stdio.h>
#include<math.h>
main()
{
/*variables*/
int x[10][10],p[10][10][10],o[10][10],i,j,k,a,b,c,n,num,nz,tempi,tempj,tempk,bi,bj,i1,j1,k1,i11,j11,bi1,bj1,row[10][10],rown[10][10],col[10][10],coln[10][10],box[10][10][10],boxn[10][10][10],m,mat[10];

/*initializingzing values*/
for(k=1;k<=9;k++)
{
for(i=1;i<=9;i++)
{
for(j=1;j<=9;j++)
{
p[k][i][j]=1;
}
}
}
for(i=1;i<=9;i++)
{
for(j=1;j<=9;j++)
{
x[i][j]=0;
o[i][j]=0;
}
}

/*input*/
printf("how many numbers are present initially?");
scanf("%d",&n);
for(i=1;i<=n;i++)
{
printf("enter coordinates [x,y]");
scanf("%d%d",&a,&b);
printf("enter the number");
scanf("%d",&x[a][b]);
num=x[a][b];
o[a][b]=1;
for(j=1;j<=9;j++)
{
p[num][a][j]=0;
p[num][j][b]=0;
}
for(k=1;k<=9;k++)
{
p[k][a][b]=0;
}
if(a<=3)
{
bi=0;
}
else if(a<=6)
{
bi=1;
}
else
{
bi=2;
}
if(b<=3)
{
bj=0;
}
else if(b<=6)
{
bj=1;
}
else
{
bj=2;
}
for(i11=3*bi+1;i11<=3*bi+3;i11++)
{
for(j11=3*bj+1;j11<=3*bj+3;j11++)
{
p[num][i11][j11]=0;
}
}
}

for(c=1;c<=65;c++)
{

/*row check*/
for(k=1;k<=9;k++)
{
for(i=1;i<=9;i++)
{
nz=0;
for(j=1;j<=9;j++)
{
if(p[k][i][j]==0)
{
nz=nz+1;
}
else
{
tempi=i;
tempj=j;
}
}                               /*end of j loop*/
if(nz==8)
{
x[tempi][tempj]=k;
for(i1=1;i1<=9;i1++)
{
p[k][tempi][i1]=0;
p[k][i1][tempj]=0;
}
for(k1=1;k1<=9;k1++)
{
p[k1][tempi][tempj]=0;
}
if(tempi<=3)
{
bi=0;
}
else if(tempi<=6)
{
bi=1;
}
else
{
bi=2;
}
if(tempj<=3)
{
bj=0;
}
else if(tempj<=6)
{
bj=1;
}
else
{
bj=2;
}
for(i11=3*bi+1;i11<=3*bi+3;i11++)
{
for(j11=3*bj+1;j11<=3*bj+3;j11++)
{
p[k][i11][j11]=0;
}
}
}                               /*end of if loop*/
}                               /*end of i loop*/
}                               /*end of k loop*/

/*column check*/
for(k=1;k<=9;k++)
{
for(j=1;j<=9;j++)
{
nz=0;
for(i=1;i<=9;i++)
{
if(p[k][i][j]==0)
{
nz=nz+1;
}
else
{
tempi=i;
tempj=j;
}
}                               /*end of i loop*/
if(nz==8)
{
x[tempi][tempj]=k;
for(i1=1;i1<=9;i1++)
{
p[k][tempi][i1]=0;
p[k][i1][tempj]=0;
}
for(k1=1;k1<=9;k1++)
{
p[k1][tempi][tempj]=0;
}
if(tempi<=3)
{
bi=0;
}
else if(tempi<=6)
{
bi=1;
}
else
{
bi=2;
}
if(tempj<=3)
{
bj=0;
}
else if(tempj<=6)
{
bj=1;
}
else
{
bj=2;
}
for(i11=3*bi+1;i11<=3*bi+3;i11++)
{
for(j11=3*bj+1;j11<=3*bj+3;j11++)
{
p[k][i11][j11]=0;
}
}
}                               /*end of if*/
}                               /*end of j loop*/
}                               /*end of k loop*/

/*box check*/
for(k=1;k<=9;k++)
{
for(bi=0;bi<=2;bi++)
{
for(bj=0;bj<=2;bj++)
{
nz=0;
for(i=3*bi+1;i<=3*bi+3;i++)
{
for(j=3*bj+1;j<=3*bj+3;j++)
{
if(p[k][i][j]==0)
{
nz=nz+1;
}
else
{
tempi=i;
tempj=j;
}
}                               /*i loop*/
}                               /*j loop*/
if(nz==8)
{
x[tempi][tempj]=k;
for(i1=1;i1<=9;i1++)
{
p[k][tempi][i1]=0;
p[k][i1][tempj]=0;
}
for(k1=1;k1<=9;k1++)
{
p[k1][tempi][tempj]=0;
}
if(tempi<=3)
{
bi1=0;
}
else if(tempi<=6)
{
bi1=1;
}
else
{
bi1=2;
}
if(tempj<=3)
{
bj1=0;
}
else if(tempj<=6)
{
bj1=1;
}
else
{
bj1=2;
}
for(i11=3*bi1+1;i11<=3*bi1+3;i11++)
{
for(j11=3*bj1+1;j11<=3*bj1+3;j11++)
{
p[k][i11][j11]=0;
}
}
}                               /*end of if*/
}                               /*end of bj loop*/
}                               /*end of bi loop*/
}                               /*end of k loop*/

/*position check*/
for(i=1;i<=9;i++)
{
for(j=1;j<=9;j++)
{
nz=0;
for(k=1;k<=9;k++)
{
if(p[k][i][j]==0)
{
nz=nz+1;
}
else
{
tempk=k;
}
}                               /*end of k loop*/
if(nz==8)
{
x[i][j]=tempk;
p[tempk][i][j]=0;
for(i1=1;i1<=9;i1++)
{
p[tempk][i1][j]=0;
p[tempk][i][i1]=0;
p[i1][i][j]=0;
}
if(i<=3)
{
bi=0;
}
else if(i<=6)
{
bi=1;
}
else
{
bi=2;
}
if(j<=3)
{
bj=0;
}
else if(j<=6)
{
bj=1;
}
else
{
bj=2;
}
for(i11=3*bi+1;i11<=3*bi+3;i11++)
{
for(j11=3*bj+1;j11<=3*bj+3;j11++)
{
p[tempk][i11][j11]=0;
}
}
}                               /*end of decisive if*/
}                               /*end of j loop*/
}                               /*end of i loop*/

/*extra logic*/
/*row initialization*/
for(k=1;k<=9;k++)
{
for(i=1;i<=9;i++)
{
row[k][i]=0;
rown[k][i]=0;
for(j=1;j<=9;j++)
{
row[k][i]=row[k][i]+p[k][i][j]*pow(10,j-1);
rown[k][i]=rown[k][i]+p[k][i][j];
}
}
}
/*column initialization*/
for(k=1;k<=9;k++)
{
for(j=1;j<=9;j++)
{
col[k][j]=0;
coln[k][j]=0;
for(i=1;i<=9;i++)
{
col[k][j]=col[k][j]+p[k][i][j]*pow(10,i-1);
coln[k][j]=coln[k][j]+p[k][i][j];
}
}
}
/*box initialization*/
for(k=1;k<=9;k++)
{
for(bi=0;bi<=2;bi++)
{
for(bj=0;bj<=2;bj++)
{
box[k][bi][bj]=0;
boxn[k][bi][bj]=0;
a=0;
for(i=3*bi+1;i<=3*bi+3;i++)
{
for(j=3*bj+1;j<=3*bj+3;j++)
{
a=a+1;
box[k][bi][bj]=box[k][bi][bj]+p[k][i][j]*pow(10,a-1);
boxn[k][bi][bj]=boxn[k][bi][bj]+p[k][i][j];
}
}
}
}
}

/*row d-check*/
for(i=1;i<=9;i++)
{
for(k1=1;k1<=8;k1++)
{
for(i1=1;i1<=9;i1++)
{
mat[i1]=0;
}
m=1;
mat[k1]=1;
for(k=k1+1;k<=9;k++)
{
if(row[k][i]==row[k1][i])
{
m=m+1;
mat[k]=1;
}
}                                                     /*end of k loop*/
if(m==rown[k1][i])
{
for(k=1;k<=9;k++)
{
for(j=1;j<=9;j++)
{
if(o[i][j]==0 && mat[k]==0)
{
if(p[k1][i][j]==1)
{
p[k][i][j]=0;
}
}
}
}
}                                                      /*end of if*/
}
}

/*column d-check*/
for(j=1;j<=9;j++)
{
for(k1=1;k1<=8;k1++)
{
for(i1=1;i1<=9;i1++)
{
mat[i1]=0;
}
m=1;
mat[k1]=1;
for(k=k1+1;k<=9;k++)
{
if(col[k][j]==col[k1][j])
{
m=m+1;
mat[k]=1;
}
}                                                     /*end of k loop*/
if(m==coln[k1][j])
{
for(k=1;k<=9;k++)
{
for(i=1;i<=9;i++)
{
if(o[i][j]==0 && mat[k]==0)
{
if(p[k1][i][j]==1)
{
p[k][i][j]=0;
}
}
}
}
}                                                      /*end of if*/
}
}

/*box d-check*/
for(bi=0;bi<=2;bi++)
{
for(bj=0;bj<=2;bj++)
{
for(k1=1;k1<=8;k1++)
{
for(i1=1;i1<=9;i1++)
{
mat[i1]=0;
}
m=1;
mat[k1]=1;
for(k=k1+1;k<=9;k++)
{
if(box[k][bi][bj]==box[k1][bi][bj])
{
m=m+1;
mat[k]=1;
}
}                                                     /*end of k loop*/
if(m==boxn[k1][bi][bj])
{
for(k=1;k<=9;k++)
{
for(i=3*bi+1;i<=3*bi+3;i++)
{
for(j=3*bj+1;j<=3*bj+3;j++)
{
if(o[i][j]==0 && mat[k]==0)
{
if(p[k1][i][j]==1)
{
p[k][i][j]=0;
}
}
}
}
}
}                                                      /*end of if*/
}
}
}






}                                                      /*end of c loop*/

/*output*/
printf("\n");
printf("********************************* \n");
for(bi=0;bi<=2;bi++)
{
for(i11=3*bi+1;i11<=3*bi+3;i11++)
{
for(bj=0;bj<=2;bj++)
{
printf("*");
for(j11=3*bj+1;j11<=3*bj+3;j11++)
{
printf("%3d",x[i11][j11]);
}
printf("*");
}
printf("\n");
}
printf("********************************* \n");
}


}


                  