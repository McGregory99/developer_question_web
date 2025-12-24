import "react";
import { SignIn, SignUp, SignedIn, SignedOut } from "@clerk/clerk-react";

export default function AuthenticationPage() {
    return (
        <div className="auth-container">
            <SignedOut>
                {/* if the user is Signed Out he will see this */}
                <SignIn routing="path" path="/sign-in" />
                <SignUp routing="path" path="/sign-up" />
            </SignedOut>
            <SignedIn>
                {/* if the user is Signed In he will see this */}
                <div className="redirect-message">
                    You are already signed in. Redirecting to the home page...
                </div>
            </SignedIn>
        </div>
    );
}
