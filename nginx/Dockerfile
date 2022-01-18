FROM public.ecr.aws/ubuntu/nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
ENV TZ Asia/Seoul
CMD ["nginx", "-g", "daemon off;"]