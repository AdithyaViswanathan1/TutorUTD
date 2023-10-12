import { Component, Input, OnChanges, SimpleChanges } from "@angular/core";

@Component({
    selector: 'app-navbar',
    templateUrl: './navbar.component.html',
    styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnChanges{
    constructor() {
        this.loggedIn = false;
    }

    @Input() loggedIn: boolean
    
    ngOnChanges(changes: SimpleChanges): void {
        throw new Error("Method not implemented.");
    }
    
}