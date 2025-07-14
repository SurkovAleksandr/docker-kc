for i in 1 2 3 4 5 6; do
  echo $i
done

name=$1
len=${#name}
first_letter=${name::1}
rest_letters=${name:1:len}
if [ -z "$name" ]; then
    echo "Нужно ввести аргумент"
    exit 1
else
  echo "Hello, ${first_letter^}${rest_letters,,} :)"
fi
