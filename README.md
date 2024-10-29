# Contact Management System




## Overview

The Contact Management System is a full-stack web application that allows users to register, login, manage their contact information, and search for contacts using registration numbers. The system consists of a React-based frontend and a Flask-based backend with MongoDB as the database.

## Features

- User Authentication (Register, Login, Forgot Password)
- Contact Information Management
- Contact Search Functionality
- Responsive Design

## Tech Stack

### Frontend
- React.js
- Next.js (App Router)
- Tailwind CSS
- shadcn/ui components

### Backend
- Flask
- MongoDB
- PyJWT for authentication
- Flask-Bcrypt for password hashing

## Project Structure
project/
├── frontend/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── login/
│   │   │   └── page.tsx
│   │   ├── contact-form/
│   │   │   └── page.tsx
│   │   └── search/
│   │       └── page.tsx
│   └── components/
│       └── ui/
│           └── (shadcn/ui components)
└── backend/
├── app.py
├── config.py
├── requirements.txt
├── models/
│   └── user.py
├── routes/
│   ├── auth.py
│   └── contact.py
├── services/
│   ├── auth_service.py
│   └── contact_service.py
└── utils/
└── email_utils.

## Setup and Installation

### Frontend

1. Navigate to the frontend directory:
...

The frontend will be available at \`http://localhost:3000\`.

### Backend

1. Navigate to the backend directory:
2. Create a virtual environment:
python -m venv venv
```bash
source venv/bin/activate
```
### Install dependencies:

```bash
pip install -r requirements.txt
```


4. Set up environment variables:
Create a \`.env\` file in the backend directory with the following content:
```bash
SECRET_KEY=your-secret-key
MONGO_URI=your-mongodb-uri
JWT_SECRET_KEY=your-jwt-secret-key
```
5. Run the Flask application:
```bash
python3 app.py
```


The backend API will be available at \`http://localhost:5000\`.

## API Endpoints

- POST \`/auth/register\`: Register a new user
- POST \`/auth/login\`: Login a user
- POST \`/auth/forgot-password\`: Initiate password reset
- POST \`/contact/add\`: Add a new contact
- GET \`/contact/search\`: Search for a contact by registration number

## Frontend Routes

- \`/\`: Login page
- \`/contact-form\`: Contact information form
- \`/search\`: Contact search page

## Component Details

### Frontend

1. \`app/layout.tsx\`: Root layout component
2. \`app/page.tsx\`: Main page (redirects to login)
3. \`app/login/page.tsx\`: Login component
4. \`app/contact-form/page.tsx\`: Contact form component
5. \`app/search/page.tsx\`: Search component

### Backend

1. \`app.py\`: Main Flask application
2. \`config.py\`: Configuration settings
3. \`models/user.py\`: User model
4. \`routes/auth.py\`: Authentication routes
5. \`routes/contact.py\`: Contact management routes
6. \`services/auth_service.py\`: Authentication service
7. \`services/contact_service.py\`: Contact management service
8. \`utils/email_utils.py\`: Email utility functions

## Code Snippets

### Frontend Example (Login Component)

\`\`\`tsx
'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { AlertCircle } from "lucide-react"

export default function LoginPage() {
const [username, setUsername] = useState('')
const [password, setPassword] = useState('')
const [error, setError] = useState('')
const [resetEmailSent, setResetEmailSent] = useState(false)
const router = useRouter()

const handleLogin = async (e: React.FormEvent) => {
 e.preventDefault()
 // Here you would typically make an API call to verify credentials
 if (username === 'user' && password === 'password') {
   router.push('/contact-form')
 } else {
   setError('Invalid username or password')
 }
}

const handleForgotPassword = async () => {
 // Here you would typically make an API call to send a reset email
 setResetEmailSent(true)
}

return (
 <div className="flex items-center justify-center min-h-screen bg-gray-100">
   <Card className="w-[350px]">
     <CardHeader>
       <CardTitle>Login</CardTitle>
       <CardDescription>Enter your username and password to access your account.</CardDescription>
     </CardHeader>
     <CardContent>
       <form onSubmit={handleLogin}>
         <div className="grid w-full items-center gap-4">
           <div className="flex flex-col space-y-1.5">
             <Label htmlFor="username">Username</Label>
             <Input 
               id="username" 
               value={username}
               onChange={(e) => setUsername(e.target.value)}
               placeholder="Enter your username"
             />
           </div>
           <div className="flex flex-col space-y-1.5">
             <Label htmlFor="password">Password</Label>
             <Input 
               id="password" 
               type="password"
               value={password}
               onChange={(e) => setPassword(e.target.value)}
               placeholder="Enter your password"
             />
           </div>
         </div>
         {error && (
           <Alert variant="destructive" className="mt-4">
             <AlertCircle className="h-4 w-4" />
             <AlertTitle>Error</AlertTitle>
             <AlertDescription>{error}</AlertDescription>
           </Alert>
         )}
         <Button className="w-full mt-4" type="submit">Login</Button>
       </form>
     </CardContent>
     <CardFooter className="flex justify-between">
       <Button variant="link" onClick={handleForgotPassword}>Forgot password?</Button>
     </CardFooter>
   </Card>
   {resetEmailSent && (
     <Alert className="absolute bottom-4 right-4 w-96">
       <AlertTitle>Password Reset Email Sent</AlertTitle>
       <AlertDescription>
         Check your email for instructions to reset your password.
       </AlertDescription>
     </Alert>
   )}
 </div>
)
}
```


### Backend Example (Auth Service)


```python
from models.user import User
from app import db
import jwt
from flask import current_app
from datetime import datetime, timedelta

class AuthService:
 def register_user(self, user_data):
     if db.users.find_one({'username': user_data['username']}):
         return {'success': False, 'message': 'Username already exists'}
     if db.users.find_one({'email': user_data['email']}):
         return {'success': False, 'message': 'Email already exists'}
     
     user = User(user_data['username'], user_data['email'], user_data['password'])
     db.users.insert_one(user.to_dict())
     return {'success': True, 'message': 'User registered successfully'}

 def login_user(self, login_data):
     user_data = db.users.find_one({'username': login_data['username']})
     if not user_data:
         return {'success': False, 'message': 'User not found'}
     
     user = User.from_dict(user_data)
     if user.check_password(login_data['password']):
         token = jwt.encode({
             'username': user.username,
             'exp': datetime.utcnow() + timedelta(hours=1)
         }, current_app.config['JWT_SECRET_KEY'])
         return {'success': True, 'token': token}
     return {'success': False, 'message': 'Invalid password'}

 def user_exists(self, email):
     return db.users.find_one({'email': email}) is not None
```


## Development

- For frontend development, make changes in the \`frontend/app\` directory.
- For backend development, modify the relevant files in the \`backend\` directory.

## Testing

- Frontend: Add Jest and React Testing Library for component testing.
- Backend: Use pytest for unit and integration testing.

## Deployment

- Frontend: Deploy the Next.js application to a platform like Vercel or Netlify.
- Backend: Deploy the Flask application to a platform like Heroku or AWS.

## Security Considerations

- Ensure all sensitive information is stored securely and not exposed in the codebase.
- Implement proper input validation and sanitization on both frontend and backend.
- Use HTTPS for all communications between frontend and backend.
- Regularly update dependencies to patch any security vulnerabilities.
- Implement rate limiting on the backend to prevent abuse.
- Use secure session management and token-based authentication.

## Future Improvements

- Implement email functionality for password reset
- Add user profile management
- Enhance contact search with additional filters
- Implement pagination for large datasets
- Add data export functionality
- Implement real-time updates using WebSockets
- Add multi-factor authentication for enhanced security
- Implement a dashboard with analytics and reporting features

## Contributing

1. Fork the repository
2. Create your feature branch (\`git checkout -b feature/AmazingFeature\`)
3. Commit your changes (\`git commit -m 'Add some AmazingFeature'\`)
4. Push to the branch (\`git push origin feature/AmazingFeature\`)
5. Open a Pull Request

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Next.js documentation
- Flask documentation
- MongoDB documentation
- shadcn/ui component library
