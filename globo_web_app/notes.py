# # ejemplo de loop count 
# resource "aws_instance" "web_servers" {
#   count = 3
#   tags = {
#     "Name" = "globo-web-${count.index}"
#   }
  
# }

# # acceder a webservers 
# aws_instance.web_servers[0].tags.Name
# aws_instance.web_servers[*].tags.Name # todas las instancias


# # ejemplo de loop for_each 
# resource "aws_s3_bucket_object" "taco_toppings" {
#   for_each = {
#     cheese = "cheese.png"
#     lettuce = "lettuce.png" 
#   }
# }
# aws_s3_bucket_object.taco_toppings["cheese"].id
# aws_s3_bucket_object.taco_toppings[*].id # all instances