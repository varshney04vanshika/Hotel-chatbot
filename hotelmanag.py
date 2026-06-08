def HM():
    print("Management Team: Hello! How can I assist you today? Type 'bye' to exit")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Hotel: Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Hotel: Hello! How can I assist you today?")
        elif "book" in user_input:
            print("Hotel: You can book a room through our website or by calling our reservation line.")
        elif "amenities" in user_input:
            print("Hotel: We offer a fitness center, swimming pool, and free Wi-Fi.")
        elif "room types" in user_input or "rooms" in user_input:
            print("Hotel: We have standard rooms, deluxe rooms, and suites.")
        elif "check-in" in user_input or "check out" in user_input:
            print("Hotel: Check-in is at 3 PM and check-out is at 11 AM.")
        elif "cancellation" in user_input:
            print("Hotel: Free cancellation up to 24 hours before arrival.")
        elif "restaurant" in user_input:
            print("Hotel: Yes, we have a restaurant serving all meals.")
        elif "parking" in user_input:
            print("Hotel: Yes, parking facilities are available.")
        elif "price" in user_input:
            print("Hotel: Prices depend on room type and dates.")
        elif "address" in user_input:
            print("Hotel: We are located at 123 Main Street.")
        elif "offer" in user_input or "discount" in user_input:
            print("Hotel: We have seasonal offers. Please check our website.")
        elif "contact" in user_input:
            print("Hotel: You can contact us at (123) 456-7890 or email us at")
        elif "email" in user_input:
            print("Hotel: You can email us at Hotel123@gmail.com")
        elif "feedback" in user_input:
            print("Hotel: We value your feedback! Please share your experience with us.")
        elif "complaint" in user_input:
            print("Hotel: We're sorry to hear that. Please provide details of your complaint.")
        elif "branches" in user_input:
            print("Hotel: We have branches in Lucknow, Delhi, and Goa.")
        elif "services" in user_input:
            print("Hotel: We offer room service, laundry, and concierge services.")
        elif "events" in user_input:
            print("Hotel: We can host events. Please contact our event coordinator for more details.")
        elif "spa" in user_input:
            print("Hotel: Yes, we have a spa offering various treatments.")
        elif "gym" in user_input:
            print("Hotel: Yes, we have a fully equipped gym.")
        elif "pool" in user_input:
            print("Hotel: Yes, we have a swimming pool available for guests.")
        elif "wifi" in user_input:
            print("Hotel: Yes, we offer free Wi-Fi throughout the hotel.")
        elif "transportation" in user_input:
            print("Hotel: We offer airport shuttle services and car rentals.")
        elif "best available room" in user_input:
            print("Hotel: The best available room is our deluxe suite with a city view.")
        elif "availability" in user_input:
            print("Hotel: Please provide your desired dates for availability information.")
        elif "payment" in user_input:
            print("Hotel: We accept all major credit cards, cash, and mobile payments.")
        elif "loyalty program" in user_input:
            print("Hotel: Yes, we have a loyalty program that offers exclusive benefits and discounts.")
        else:
            print("Hotel: Sorry, I didn't understand that. Please rephrase.")
HM()