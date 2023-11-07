import { Component} from "@angular/core";
import { AuthenticationService } from "../authentication.service";
import { CookieService } from "ngx-cookie-service";
import { Router } from "@angular/router";
import { faUser, faRightFromBracket } from "@fortawesome/free-solid-svg-icons";

@Component({
    selector: 'app-navbar',
    templateUrl: './navbar.component.html',
    styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent{
    faUser = faUser;
    faRightFromBracket = faRightFromBracket;
    showPopup = false;
    
    constructor(
        private authenticationService: AuthenticationService,
        public cookieService: CookieService,
        private router: Router) {
            
        }

    toSearch()
    {
        this.router.navigate(['/search']);
    }

    toProfile()
    {
        let id = this.cookieService.get('userId');
        this.router.navigate(['/profile', id]);
    }

    toAppointments()
    {
        this.router.navigate(['/appointments']);
    }

    logout()
    {
        this.authenticationService.logout();
    }

    togglePopup()
    {
        this.showPopup = !this.showPopup;
    }
    
}