import { Injectable } from '@angular/core';
import { httpManager } from './httpManager';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  manager: httpManager;

  constructor(httpManager: httpManager) {
    this.manager = httpManager;
   }

  search(searchString : string)
  {
    return this.manager.search(searchString);
  }
}
