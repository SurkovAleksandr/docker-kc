FROM eclipse-temurin:21-alpine AS builder
LABEL authors="u-user"
WORKDIR /app
COPY src src
RUN javac ./src/Calculate.java

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=builder /app/src/Calculate.class Calculate.class
CMD ["java", "Calculate"]
